
import os
import speech_recognition as sr

from qt_core import *
from ffmpy import FFmpeg
from modules import Settings_Json
from audioclipextractor import AudioClipExtractor

from . thread import Runner
from PyQt5.QtCore import QThreadPool


class StopTranscription(BaseException):
    pass


def duration_detector(length) -> tuple:
    hours = length // 3600  # calculate in hours
    length %= 3600
    mins = length // 60  # calculate in minutes
    length %= 60
    seconds = length  # calculate in seconds

    return hours, mins, seconds


class TranscribeEngine:
    def __init__(self):
        self.__recognizer = sr.Recognizer()
        self.standard_format = ".wav"
        self.accepted_length = 50

        self.__thread_pool = QThreadPool()
        self.__thread_pool.setMaxThreadCount(3)

        self.__create_audio_folder()

        self.__ffmeg_path = "ffmpeg_engine/bin/ffmpeg"

        # add to Path
        abs_path = os.path.abspath("ffmpeg_engine\\bin")
        os.environ['PATH'] = abs_path + os.pathsep + os.environ['PATH']
        os.environ['PATH'] = os.environ['PATH']

        self.settings = Settings_Json().items

        self.__houndify_details = {
            "client_id": self.settings["houndify"]["client_id"],
            "client_key": self.settings["houndify"]["client_key"]
        }

    def threadpool(self):
        return self.__thread_pool

    def __create_audio_folder(self):
        audio_folder = "converted_audio"
        if os.path.exists(audio_folder):
            self.path_to_converted_audio = os.path.abspath(audio_folder)
        else:
            os.makedirs(audio_folder)
            self.path_to_converted_audio = os.path.abspath(audio_folder)

    @staticmethod
    def detect_file_format(fname):
        basename, ext = os.path.basename(fname), os.path.splitext(fname)[-1].lower()

        valid_audio_format = ('.mp3', '.wav', '.ogg', '.ogx', '.aiff', '.mp2', '.3gp', '.flac')
        valid_movie_format = ('.mp4', '.avi', '.mkv', )

        report = {'is_audio': False, 'is_format': False}

        if ext in valid_audio_format:
            report['is_audio'] = True
            if ext == '.flac':
                report['is_format'] = True
        elif ext in valid_movie_format:
            report['is_audio'] = False
            report['is_format'] = False
        else:
            raise ValueError("Unknown format detected: file is not a video or an audio")

        return report

    @staticmethod
    def __format_converter(inputs, outputs):
        clip = FFmpeg(inputs={inputs: None},
                      outputs={outputs: None})
        clip.run()

    def __convert_video_to_audio(self, *, fname):
        audio_file = os.path.basename(fname)
        audio_file, ext = os.path.splitext(audio_file)
        audio_file = os.path.join(self.path_to_converted_audio, audio_file)
        audio_file = f"{audio_file}{self.standard_format}"

        if os.path.exists(audio_file):
            # delete the file, this current file might be
            # an updated version
            os.remove(audio_file)
        self.__format_converter(fname, audio_file)

        return audio_file

    def __convert_audio_to_wav_format(self, *, fname):
        audio_file = os.path.basename(fname)
        audio_file, ext = os.path.splitext(audio_file)
        audio_file = os.path.join(self.path_to_converted_audio, audio_file)
        audio_file = f"{audio_file}{self.standard_format}"

        if os.path.exists(audio_file):
            # delete the file, this current file might be
            # an updated version
            os.remove(audio_file)
        self.__format_converter(fname, audio_file)

        return audio_file

    def convert_to_required_format(self, parent, *, report: dict, fname: str, silent_progress=False):
        if not report['is_audio']:
            if not silent_progress:
                parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][fname]['progress_info'] = "video to proper format"
                parent.signals.progress_signal.emit()
            audio_path = self.__convert_video_to_audio(fname=fname)
        else:
            if not report['is_format']:
                if not silent_progress:
                    parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][fname]['progress_info'] = "audio to proper format"
                    parent.signals.progress_signal.emit()
                audio_path = self.__convert_audio_to_wav_format(fname=fname)
            else:
                audio_path = fname

        return audio_path

    def __google_web_speech(self, old_fname, fname, audio_length, parent, *, previous_batch=0, text=[]):
        """Uses Google web speech api to transcribe the audio 100 sec interval at a time

        Args:
            old_fname (str): The absolute file path of the audio in it original format
            fname (str): The absolute file path of the audio that has been converted to the wav format
            audio_length (int): The duration of the audio in seconds
            parent (_type_): An access point of the 
            previous_batch (int, optional): The offset of the audio. Defaults to 0.

        Returns:
            str: The transcribed text
        """
        file_interval = 100
        total_text = text

        with sr.AudioFile(fname) as source:
            for batch in range(previous_batch, int(audio_length), file_interval):
                if parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][old_fname]['pause']:
                    information = {
                        'old_fname': old_fname,
                        'new_fname': fname,
                        'pause_time': batch,
                        'selected_api': "Google Speech Recognition",
                        'text': total_text
                    }
                    
                    parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][old_fname]['pause'] = information
                    parent.ui.continue_transcription.setHidden(False)
                    parent.ui.continue_transcription.setDisabled(False)
                    parent.ui.internet_connectivity_display.setHidden(False)
                    
                    raise StopTranscription("Transcription pause button clicked")
                try:
                    init_hour, init_mins, init_sec = duration_detector(batch)
                    final_hour, final_mins, final_sec = duration_detector(batch + file_interval)
                    
                    parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][old_fname]['progress_info'] = batch
                    parent.signals.progress_signal.emit()
                    
                    audio = self.__recognizer.record(source, offset=previous_batch, duration=file_interval)
                    text = self.__recognizer.recognize_google(audio)
                    
                    # divide into every 5mins
                    if init_mins % 5 == 0:
                        text = f"\n\n----{init_hour}:{init_mins}:{init_sec} \n{text}"
                        
                    if final_mins % 5 == 0:
                        text = f"{text}\n {final_hour}:{final_mins}:{final_sec}\n\n"

                except Exception as e:
                    init_hour, init_mins, init_sec = duration_detector(batch)
                    final_hour, final_mins, final_sec = duration_detector(batch + file_interval)
                    text = f"---{init_hour}:{init_mins}:{init_sec}  An error occurred here: " \
                           f"{final_hour}:{final_mins}:{final_sec} ---"
                total_text.append(text)

            total_text = " ".join(total_text)
            return total_text

    def __houndify(self, old_fname, fname, audio_length, parent, *, previous_batch=0, text=[]) -> str:
        file_interval = 40
        total_text = text

        with sr.AudioFile(fname) as source:
            for batch in range(0, int(audio_length), file_interval):
                if parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][old_fname]['pause']:
                    information = {
                        'old_fname': old_fname,
                        'new_fname': fname,
                        'pause_time': batch,
                        'selected_api': "Google Speech Recognition",
                        'text': total_text
                    }

                    parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][old_fname]['pause'] = information
                    parent.ui.continue_transcription.setHidden(False)
                    parent.ui.continue_transcription.setDisabled(False)
                    parent.ui.internet_connectivity_display.setHidden(False)

                    raise StopTranscription("Transcription pause button clicked")
                try:
                    init_hour, init_mins, init_sec = duration_detector(batch)
                    final_hour, final_mins, final_sec = duration_detector(batch + file_interval)
                    
                    parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][old_fname]['progress_info'] = batch + previous_batch
                    parent.signals.progress_signal.emit()
                    
                    audio = self.__recognizer.record(source, duration=file_interval)
                    text = self.__recognizer.recognize_houndify(audio, self.__houndify_details['client_id'],
                                                                self.__houndify_details['client_key'])

                    # divide into every 5mins
                    if init_mins % 5 == 0:
                        text = f"\n\n----{init_hour}:{init_mins}:{init_sec} \n{text}"
                        
                    if final_mins % 5 == 0:
                        text = f"{text}\n {final_hour}:{final_mins}:{final_sec}\n\n"

                except Exception:
                    init_hour, init_mins, init_sec = duration_detector(batch)
                    final_hour, final_mins, final_sec = duration_detector(batch + file_interval)
                    text = f"\n\n---{init_hour}:{init_mins}:{init_sec}  An error occurred here " \
                           f"{final_hour}:{final_mins}:{final_sec} \n\n---"
                total_text.append(text)

            total_text = " ".join(total_text)
            return total_text

    def split_audio_to_standard_length(self, parent, *, fname, audio_length):
        parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][fname]['progress_info'] = "split long audio file"
        parent.signals.progress_signal.emit()

        interval = self.accepted_length * 60
        extractor = AudioClipExtractor(fname)

        # create a folder to contain the split files
        base_folder = "Split Audios"
        split_audio_folder_path = os.path.join(base_folder, os.path.basename(fname))

        if not os.path.exists(split_audio_folder_path):
            os.makedirs(split_audio_folder_path)

        specs = ""
        for rank, idx in enumerate(range(0, int(audio_length), interval)):
            start = idx
            end = idx + interval
            if end > audio_length:
                end = audio_length

            hour, mins, sec = duration_detector(start)
            hour_, mins_, sec_ = duration_detector(end)
            title = f"{int(hour)}-{int(mins)}-{int(sec)} --- {int(hour_)}-{int(mins_)}-{int(sec_)}"
            specs += f"{start}\t\t{end}\t{title}\n"

        extractor.extract_clips(specs, split_audio_folder_path, text_as_title=True)
        audio_paths = [os.path.join(split_audio_folder_path, path) for path in os.listdir(split_audio_folder_path)]

        return audio_paths

    def __transcribe(self, parent, *, fname, selected_api, ignore=None):
        """Internal method that handles the transcription of the audio and ensures
        that the audio get converted to the proper format and use the selected 
        transcription API to transcribe the audio   

        Args:
            parent: A reference to the parent widget
            fname (str): The absolute file path of the original audio
            selected_api (str): The selected Speech to Text Transcription API

        Raises:
            ValueError: Raised when code logic get to that point for some
                        unknown reason.
        """
        scriptures = "I pray to God the Father of our Lord Jesus Christ, that He takes " \
                     "away the stony heart and gives you a new heart of flesh and a new " \
                     "spirit, so that you will be able to lay aside all filthiness and " \
                     "overflow of wickedness and receive with meekness the engrafted " \
                     "Word that will be written on the fleshy table of your heart, " \
                     "which is able to save your soul.\n" \
                     "\t\tEzekiel 36:26, James 1:21, 2 Corinthians 3:3"

        if not ignore:
            audio_length = parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][fname]['full_length']
            report = self.detect_file_format(fname)
            # file_type = 'Audio' if report['is_audio'] else 'Video'

            # indicate the transcription process has started
            parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][fname]['start'] = True

            # parent.signals.progress_signal.emit("checking file format", fname)
            parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']["current_file"][fname]["progress_info"] = "checking file format"
            new_fname = self.convert_to_required_format(parent, report=report, fname=fname)
            text = []
            previous_batch = 0

        else:
            audio_length = ignore.pop('audio_length')
            new_fname = ignore.pop('new_fname')
            text = ignore.pop('text')
            previous_batch = ignore.pop('pause_time')

        try:
            if selected_api == "Google Speech Recognition":
                text = self.__google_web_speech(fname, new_fname, audio_length, parent,
                                                previous_batch=previous_batch, text=text)
            elif selected_api == "Houndify Voice Recognition":
                text = self.__houndify(fname, new_fname, audio_length, parent)
            else:
                raise ValueError("Code ought not to reach this point")

            if text:
                parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][fname]['text'] = text

            parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][fname]['finish'] = True
            parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['no_of_files_transcribed'] += 1
            parent.signals.transcription_completion_signal.emit(fname)
            print(fname, scriptures, "\n")
        except StopTranscription:
            # do something here if the transcription is paused
            # what? I don't know
            pass

    def transcribe(self, parent, *, fnames, selected_api):
        """Transcribe the audio by initializing a thread and passing it the internal
        __transcribe method and starting the thread.

        Args:
            parent: A reference to the parent widget
            fnames (str): The absolute file path of all the selected original audio
            selected_api (str): The Speech to Text API to use
        """
        for fname in fnames:
            runner = Runner(self.__transcribe, fname, selected_api, parent)
            self.__thread_pool.start(runner)

    def get_transcribe_audio(self, fname, parent) -> str:
        """Retrieve the text that has been transcribed by the selected transcription APPLICATION

        Args:
            fname (str): The absolute file path of the audio
            parent: A reference to the parent widget

        Returns:
            str: The transcribed text
        """
        try:
            data = parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][fname]['text']
        except KeyError:
            data = None

        return data
    
    def pause_resume_transcription(self, parent):
        """Resume or pause the selected transcription when the pause button is clicked

        Args:
            parent: A reference to the parent widget
        """
        fname = parent.ui.transcribe_file_list.currentItem().text()
        
        is_paused = parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][fname]['pause']
        msg = """<p><span>{}</span><br>
        <span style="color: red">This is an experimental feature, may cause crashes</span></p>"""
        if not is_paused:
            # save the current transcription progress information
            icon = QIcon(':/icons/images/icons/cil-caret-right.png')

            # Check at what stage the transcription is and only paused
            # when the transcription stage has passed the conversion stage
            progress_info = parent.custom_ui_function.file_operations.mode_settings["audio_transcribe"]["current_file"][fname]["progress_info"]

            if not isinstance(progress_info, str):
                parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][fname]['pause'] = True
                parent.ui.internet_connectivity_display.setText(msg.format("Transcription paused...Click to continue."))
                print("Connection paused")
            else:
                msg = msg.format("""<span style="color: red">Please wait until conversion of audio is complete</span>""")
                parent.ui.internet_connectivity_display.setText(msg)

        else:
            icon = QIcon(':/icons/images/icons/icon_maximize.png')
            parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][fname]['pause'] = False
            self.resume_transcription(is_paused, parent)
            parent.ui.internet_connectivity_display.setText(msg.format("Pause transcription"))
            print("Transcription resumed")

        parent.ui.continue_transcription.setIcon(icon)

    def resume_transcription(self, information: dict, parent):
        # directly start transcribing the audio from where it last stop

        fname = information.pop('old_fname')
        selected_api = information.pop('selected_api')

        audio_length = parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][fname]['full_length']
        information['audio_length'] = audio_length

        runner = Runner(self.__transcribe, fname, selected_api, parent, ignore=information)
        self.__thread_pool.start(runner, priority=3)

    def display_transcription_paused_status(self, *, fname, parent):
        is_paused = parent.custom_ui_function.file_operations.mode_settings['audio_transcribe']['current_file'][fname]['pause']

        msg = """<p><span>{}</span><br>
        <span style="color: red">This is an experimental feature, may cause crashes</span></p>"""

        if is_paused:
            icon = QIcon(':/icons/images/icons/cil-caret-right.png')
            parent.ui.internet_connectivity_display.setText(msg.format("Transcription paused...Click to continue."))
            print("Connection paused")
        else:
            icon = QIcon(':/icons/images/icons/icon_maximize.png')
            parent.ui.internet_connectivity_display.setText(msg.format("Click to pause transcription"))
            print("Transcription resumed")

        parent.ui.continue_transcription.setIcon(icon)
