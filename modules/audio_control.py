
import sys
import audioread

from qt_core import *
from widgets import PyDialog
from .ui_transcript_editor import Ui_TranscribeEditor


def _retrieve_filename(abs_path):
    return os.path.basename(abs_path)


def duration_detector(length):
    hours = length // 3600  # calculate in hours
    length %= 3600
    mins = length // 60  # calculate in minutes
    length %= 60
    seconds = length  # calculate in seconds

    return hours, mins, seconds


class AudioControl:
    def __init__(self, file_control):
        self.file_control = file_control

    def open_audio_file(self, parent):
        
        if self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['dirty_file']:
            message = "Don't you want to save this transcribed audio file before opening another file?\n"
            message += "The transcribed text will be lost if you don't save them"

            reply = self.file_control.raise_saving_message(parent, message=message)

            if reply == QMessageBox.Save:
                self.file_control.save(parent)
            elif reply == QMessageBox.Cancel:
                return

        filenames, _ = QFileDialog().getOpenFileNames(
            parent, 'Select file',
            f"""{self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['current_editing_file']
            if self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['current_editing_file'] else '.'}""",
            "audio files (*.mp3 *.wav *.ogg *.flv);;"
            "video files (*.mp4 *.avi *mkv);;"
            "audio and video files (*.mp3 *.wav *.ogg *.flv *.mp4 *.avi *.mkv)"
        )
        
        if filenames:
            # change cursor
            cursor = QCursor(Qt.BusyCursor)
            parent.setCursor(cursor)

            parent.ui.loading_files_widget.setHidden(False)
            parent.ui.loading_files_label.setText("Loading files:")
            parent.ui.loading_files_progressbar.setMaximum(len(filenames))
            parent.ui.loading_files_progressbar.setMinimum(0)
            parent.ui.loading_files_info_display.clear()

            parent.ui.transcribe_file_list.clear()
            # close any open transcribed text modeless dialogs
            opened_dialogs = parent.findChildren(PyDialog)
            if opened_dialogs:
                for dialog in opened_dialogs:
                    dialog.close()

            files_info = {}
            for index, fname in enumerate(filenames):

                # display progress on the progress bar
                parent.ui.loading_files_info_display.setText(_retrieve_filename(fname))

                with audioread.audio_open(fname) as f:
                    length = f.duration
                    channels = f.channels

                with open(fname, "rb") as f:
                    size = f.read()
                    size = self.file_control.bytes_converter(sys.getsizeof(size))

                files_info[fname] = {}
                files_info[fname]['font_size'] = 14
                files_info[fname]['font'] = None
                files_info[fname]['dirty_file'] = False
                files_info[fname]['start'] = False
                files_info[fname]['finish'] = False
                files_info[fname]['text'] = None
                files_info[fname]['txt_format_path'] = None
                files_info[fname]['progress_info'] = None
                files_info[fname]['full_length'] = length
                files_info[fname]['channels'] = channels
                files_info[fname]['size'] = size
                files_info[fname]['pause'] = None

                parent.ui.loading_files_progressbar.setValue(index + 1)
                print("God loves you")

            self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['current_file'] = files_info
            self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['current_editing_file'] = None
            self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['total_files'] = len(filenames)

            parent.ui.transcription_progressBar_2.setValue(0)
            parent.ui.transcription_progressBar_2.setHidden(True)
            parent.ui.transcribe_file_list.addItems(filenames)

            parent.ui.start_transcription_button.setHidden(False)
            parent.ui.start_transcription_button.setEnabled(True)

            parent.ui.loading_files_widget.setHidden(True)
            parent.ui.loading_files_info_display.clear()
            parent.ui.loading_files_progressbar.setValue(0)

            self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['is_transcribed'] = False

            # change cursor
            cursor = QCursor(Qt.ArrowCursor)
            parent.setCursor(cursor)

    def save_audio(self, parent):
        message = "You must transcribe an audio first, before you can save!"
        if not self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['is_transcribed']:
            QMessageBox.warning(parent, "Unable to Save", message)
            return

    def transcribe_audio(self, parent):
        # transcription engine will appear hear

        fnames = [parent.ui.transcribe_file_list.item(i).text() for i in range(len(parent.ui.transcribe_file_list))]

        parent.ui.start_transcription_button.setEnabled(False)
        self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['is_transcribed'] = True

        if fnames:
            parent.ui.loading_files_progressbar.setMaximum(len(fnames))
            parent.ui.loading_files_progressbar.setMinimum(0)
            parent.ui.loading_files_widget.setHidden(False)
            parent.ui.loading_files_label.setText("Transcribing...please wait:")

            # get the selected recognition api
            api = parent.ui.voice_recognition_api_combobox.currentText()
            self.file_control.transcribe_engine.transcribe(parent, fnames=fnames, selected_api=api)

    def display_list_widget_info(self, parent):
        try:
            fname = parent.ui.transcribe_file_list.currentItem().text()
        except AttributeError:
            parent.ui.transcribe_progress_display_4.clear()
            parent.ui.transcription_status_label_2.clear()
            return

        text = self.file_control.transcribe_engine.get_transcribe_audio(fname, parent)

        pattern = """<p style="font-size: 21px;">
        <p>Name: <span style="font-weight: bold">{fname}</span></p>
        <p>Size: <span style="font-weight: bold">{size}</span></p>
        <p>Length: <span style="font-weight: bold">{length}</span></p>
        <p>No of channel: <span style="font-weight: bold">{channel}</span></p>
        </p>
        """

        length = self.file_control.file_operations.mode_settings["audio_transcribe"]['current_file'][fname]["full_length"]
        hours, mins, seconds = duration_detector(length)
        length = f"{int(hours)}h {int(mins)}min {int(seconds)}sec"

        channel = self.file_control.file_operations.mode_settings['audio_transcribe']['current_file'][fname]['channels']
        size = self.file_control.file_operations.mode_settings['audio_transcribe']['current_file'][fname]['size']

        if self.file_control.file_operations.mode_settings["audio_transcribe"]["current_file"][fname]['start']:
            if not self.file_control.file_operations.mode_settings["audio_transcribe"]["current_file"][fname]['finish']:

                # toggle the pause transcription display on
                parent.ui.continue_transcription.setHidden(False)
                parent.ui.internet_connectivity_display.setHidden(False)
                parent.ui.continue_transcription.setDisabled(False)

                self.file_control.transcribe_engine.display_transcription_paused_status(fname=fname, parent=parent)

                status = """<span style="color: rgb(175, 175, 0); font-weight: bold;">{info}</span>"""

                progress_info = self.file_control.file_operations.mode_settings["audio_transcribe"]["current_file"][fname]["progress_info"]

                if isinstance(progress_info, str):
                    parent.ui.transcription_progressBar_2.setValue(0)
                    parent.ui.transcription_progressBar_2.setHidden(True)

                    if progress_info == "detecting file format":
                        status = status.format(info="Detecting file format...")

                    elif progress_info == "audio to proper format":
                        status = status.format(info="Converting Audio to wav format...")

                    elif progress_info == "video to proper format":
                        status = status.format(info="Converting Video file to wav audio format...")

                    elif progress_info == "split long audio file":
                        status = status.format(info="Splitting Audio file to 30min apiece")

                elif isinstance(progress_info, int):
                    parent.ui.transcription_progressBar_2.setHidden(False)

                    max_value = self.file_control.file_operations.mode_settings["audio_transcribe"]["current_file"][fname]["full_length"]
                    parent.ui.transcription_progressBar_2.setMaximum(max_value)
                    parent.ui.transcription_progressBar_2.setMinimum(0)
                    parent.ui.transcription_progressBar_2.setValue(progress_info)

                    status = status.format(info="Transcribing audio...")

            else:
                parent.ui.transcription_progressBar_2.setValue(0)
                parent.ui.transcription_progressBar_2.setHidden(True)

                # toggle the pause transcription display off
                parent.ui.continue_transcription.setHidden(True)
                parent.ui.internet_connectivity_display.setHidden(True)
                parent.ui.continue_transcription.setDisabled(True)

                if text:
                    status = f"<span style=\"color: green; font-weight: bold;\">Completed</span><br /><hr />" \
                             f"<p style=\"font-weight: normal;\">{text[:100]}...</p>"

        else:
            parent.ui.transcription_progressBar_2.setValue(0)
            parent.ui.transcription_progressBar_2.setHidden(True)

            # toggle the pause transcription display on
            parent.ui.continue_transcription.setHidden(True)
            parent.ui.internet_connectivity_display.setHidden(True)
            parent.ui.continue_transcription.setDisabled(True)

            if text:
                status = text
            else:
                status = "<span style=\"color: red; font-weight: bold;\">Transcription not started</span>"

        fname = os.path.basename(fname)
        parent.ui.transcribe_progress_display_4.setText(pattern.format(fname=fname, size=size, status=status,
                                                                       length=length, channel=channel))
        if status:
            parent.ui.transcription_status_label_2.setText(f"<p>Transcription status: {status} </p>")

    def edit_transcribed_text(self, parent):
        # Get currently selected file
        print("I pray that the God of our Lord Jesus Christ, the Father of Glory give "
              "to you the Spirit of wisdom and revelation in the knowledge of Him. \n"
              "That the eyes of your understanding should be enlightened, so that "
              "you should know the hope of His calling and the riches in glory of "
              "His inheritance in the saint\n "
              "\t\t Ephesian 1: 17-18")

        fname = parent.ui.transcribe_file_list.currentItem().text()

        text = self.file_control.transcribe_engine.get_transcribe_audio(fname, parent)

        if text and self.file_control.file_operations.mode_settings["audio_transcribe"]['current_file'][fname]['finish']:
            editor_ui = Ui_TranscribeEditor()
            self.editor_dialog = PyDialog(parent, editor_ui, fname_abs_path=fname)

            # TODO: Ensure that a transcribed file doubled clicked multiple time opens the same dialog

            self.editor_dialog.setWindowTitle(os.path.basename(fname))

            editor_ui.edit_transcribed_text_edit.setPlainText(
                self.file_control.file_operations.mode_settings["audio_transcribe"]['current_file'][fname]['text'])
            self.file_control.file_operations.mode_settings["audio_transcribe"]['current_editing_file'] = fname

            self.editor_dialog.show()

    def display_transcription_progress(self, parent):
        parent.ui.loading_files_widget.setHidden(False)
        parent.ui.loading_files_label.setText("Transcribing...please wait:")

        current_value = self.file_control.file_operations.mode_settings['audio_transcribe']['no_of_files_transcribed']

        parent.ui.loading_files_progressbar.setValue(current_value)

        if self.file_control.file_operations.mode_settings['audio_transcribe']['total_files'] == current_value:
            parent.ui.loading_files_widget.setHidden(True)
            parent.ui.loading_files_progressbar.setValue(0)
