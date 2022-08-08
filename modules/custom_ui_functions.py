"""
Insert Custom widgets
"""
import os

from qt_core import *

from .app_settings import Themes
from .database_operations import DataBase
from .text_control import TextControl
from .audio_control import AudioControl
from .transcriber_engine import TranscribeEngine


def _retrieve_filename(abs_path):
    return os.path.basename(abs_path)


class Files:
    def __init__(self):
        self.themes = Themes()
        self.database = DataBase()
        self.database.connect_to_db()
        self.database.connect_to_db_using_qt()
        self.transcribe_engine = TranscribeEngine()

        # which mode the user is on
        # the mode are {text file editing, search interface, audio transcribing}
        self.file_operations = FilesOperations()
        self.text_control = TextControl(self)
        self.audio_control = AudioControl(self)

    @staticmethod
    def raise_saving_message(parent, *, message):
        # one of them must be dirty, else this function won't be
        # called in the first place
        reply = QMessageBox.question(parent, 'Save file?', message,
                                     QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
                                     QMessageBox.Save)
        return reply

    def open(self, parent):
        if self.file_operations.mode == 'file_editing':
            self.text_control.open_text_file(parent)
        elif self.file_operations.mode == 'audio_transcribe':
            self.audio_control.open_audio_file(parent)
        else:
            return

        current_file = self.file_operations.mode_settings[self.file_operations.mode]['current_file']

        if current_file:
            self.toggle_dirty_state(dirty=False, parent=parent)

    def new(self, parent):
        self.text_control.new(parent)

    def save(self, parent):
        if self.file_operations.mode == 'file_editing':
            self.text_control.save_text(parent)
        elif self.file_operations.mode == 'audio_transcribe':
            self.audio_control.save_audio(parent)

    def toggle_dirty_state(self, *, dirty, parent):
        if self.file_operations.mode != 'file_search':
            if self.file_operations.mode == 'file_editing':
                self.file_operations.mode_settings[self.file_operations.mode]['dirty_file'] = dirty
            elif self.file_operations.mode == 'audio_transcribe':
                if self.file_operations.mode_settings[self.file_operations.mode]['current_editing_file']:
                    current_file = self.file_operations.mode_settings[self.file_operations.mode]['current_editing_file']
                    self.file_operations.mode_settings[self.file_operations.mode]['current_file'][current_file][
                        'dirty_file'] = dirty

        self.file_operations.handle_title_info(parent)

    def detect_text_changed(self, parent):
        self.text_control.text_validators.ensure_message_text_is_not_empty(parent)
        self.toggle_dirty_state(dirty=True, parent=parent)

    def adjust_editor_font_size(self, parent):
        # show notification
        parent.ui.adjust_text_size_label.setText(f"Size: {parent.ui.adjust_text_size.value()}")
        style_sheet = f"background-color: rgb(33, 37, 43); font-size: {parent.ui.adjust_text_size.value()}px;"

        if self.file_operations.mode == 'file_editing':
            # adjust the editor font size
            parent.ui.text_editor.setFontPointSize(parent.ui.adjust_text_size.value())
            self.file_operations.mode_settings[self.file_operations.mode]['font_size'] = parent.ui.adjust_text_size.value()

        elif self.file_operations.mode == 'audio_transcribe':

            # Get the identity of the editor that is currently requesting
            # a font change
            fname = self.file_operations.mode_settings["audio_transcribe"]["current_editing_file"]

            if fname:
                opened_dialogs = parent.findChildren(PyDialog)
                guilty_dialogs = [editor for editor in opened_dialogs if editor.fname_abs_path == fname]

                if len(guilty_dialogs) > 1:
                    raise AssertionError("There can not be more than one open editor with the same file name")
                guilty_dialogs = guilty_dialogs[0]

                # Get the editor layered out in the dialog
                text_editor = guilty_dialogs.findChild(QTextEdit)

                text_editor.setFontPointSize(parent.ui.adjust_text_size.value())
                self.file_operations.mode_settings[self.file_operations.mode]['current_file'][fname]['font_size'] = parent.ui.adjust_text_size.value()

    @staticmethod
    def __date_confirmation(button, *, parent):
        parent.accept() if button.text() == "OK" else parent.reject()

    def select_date(self, parent, *, mode):
        dialog = QDialog(parent.ui.date_edit)
        dialog.setWindowFlag(Qt.FramelessWindowHint)
        dialog.setStyleSheet("background-color: white;")

        calendar = QCalendarWidget()
        calendar.setGridVisible(True)
        font = QFont()
        font.setFamily("Verdana")

        # calendar.setStyleSheet("color: black")

        format = QTextCharFormat()
        format.setFontPointSize(13)
        format.setFontItalic(True)

        format.setBackground(QColor(self.themes.items['app_color']['dark_one']))
        calendar.setHeaderTextFormat(format)

        buttons = QDialogButtonBox()
        buttons.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        buttons.setStyleSheet(f"width: 60px; height: 25px; "
                              f"background-color: {self.themes.items['app_color']['red']}")
        buttons.clicked.connect(lambda button: self.__date_confirmation(button, parent=dialog))

        layout = QGridLayout()
        layout.addWidget(calendar, 0, 0, 1, 5)
        layout.addWidget(buttons, 1, 0, 1, 5)
        dialog.setLayout(layout)

        if dialog.exec_():
            date = calendar.selectedDate()
            date = f"GLH-{date.toString('ddd d MMM, yyyy')}-"

            if mode == 'text':
                parent.ui.text_unique_identifier.setText(date)
                self.text_control.confirm_unique_identifier(parent)
            elif mode == 'transcribe':
                parent.ui.transcribe_date_label.setText(date)

            return

    @staticmethod
    def bytes_converter(file_bytes_size: int) -> str:
        """
        Convert the file_bytes to it appropriate value in KB, MB or GB
        :param file_bytes_size: int
        :return:
        """
        kb = 1024
        mb = 1048576
        if file_bytes_size < kb:
            return f"{file_bytes_size:,.3f} bytes"
        elif kb <= file_bytes_size < mb:
            size = file_bytes_size / kb
            size = f"{size:,.2f} KB"
            return size
        elif file_bytes_size >= mb:
            size = file_bytes_size / mb
            size = f"{size:,.2f} MB"
            return size
        else:
            gb = 1073741824
            size = file_bytes_size / gb
            size = f"{size:,.2f} GB"
            return size

    def display_list_widget_info(self, parent):
        self.audio_control.display_list_widget_info(parent)

    def select_font(self, parent):
        if self.file_operations.mode in ['file_editing', 'audio_transcribe']:
            font, ok = QFontDialog(parent).getFont(parent.ui.text_editor.font())

            if ok:
                # Save this information
                self.file_operations.mode_settings[self.file_operations.mode]['font_size'] = font.pointSize()
                self.file_operations.mode_settings[self.file_operations.mode]['font'] = font.family()

                if self.file_operations.mode == 'file_editing':
                    # QTextEdit.setCurrentFont()
                    parent.ui.text_editor.setCurrentFont(font)
                elif self.file_operations.mode == 'audio_transcribe':
                    # Get the identity of the editor that is currently requesting
                    # a font change
                    fname = self.file_operations.mode_settings["audio_transcribe"]["current_editing_file"]

                    if fname:
                        opened_dialogs = parent.findChildren(PyDialog)
                        guilty_dialogs = [editor for editor in opened_dialogs if editor.fname_abs_path == fname]

                        if len(guilty_dialogs) > 1:
                            raise AssertionError("There can not be more than one open editor with the same file name")
                        guilty_dialogs = guilty_dialogs[0]

                        # Get the editor layered out in the dialog
                        text_editor = guilty_dialogs.findChild(QTextEdit)

                        text_editor.setFontPointSize(parent.ui.adjust_text_size.value())
                        self.file_operations.mode_settings[self.file_operations.mode]['current_file'][fname][
                            'font_size'] = parent.ui.adjust_text_size.value()

    def transcribe_audio(self, parent):
        self.audio_control.transcribe_audio(parent)

    def edit_transcribed_text(self, parent):
        self.audio_control.edit_transcribed_text(parent)

    def display_transcription_progress(self, parent):
        self.audio_control.display_transcription_progress(parent)

    def toggle_additional_information_frame(self, parent):
        value = parent.ui.additional_information_frame.isHidden()
        if not value:
            parent.ui.file_editing_main_layout.setContentsMargins(20, -1, -1, -1)
            icon = QIcon(u":/icons/images/icons/cil-arrow-circle-right.png")
        else:
            parent.ui.file_editing_main_layout.setContentsMargins(-1, -1, -1, -1)
            icon = QIcon(u":/icons/images/icons/cil-arrow-circle-left.png")

        parent.ui.show_additional_information_frame_push_button.setIcon(icon)
        parent.ui.additional_information_frame.setHidden(not value)


class FilesOperations:
    def __init__(self):
        """A class of the most important functionalities
        It handles the dynamic states of the application by ensuring
        that the current interface is provided with the appropriate
        settings.

        """
        self.__mode = 'file_editing'
        self.__mode_settings = {
            'file_editing': {
                'font_size': 14, 'font': None, 'dirty_file': False,
                'current_file': None, 'previous_file': None, 'file_encoding': None},

            'file_search': {'font_size': 14},

            'audio_transcribe': {
                'font_size': 14, 'font': None, 'dirty_file': False,
                'current_file': None, 'previous_file': None,
                'current_editing_file': None, 'is_transcribed': False,
                'total_files': 0, "no_of_files_transcribed": 0,
                'pause': None
            },
            'mode_memory': self.__mode
        }

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, value):
        self.__mode = value

    @property
    def mode_settings(self):
        return self.__mode_settings

    def restore_mode_settings(self, parent):
        if self.mode == "file_editing":
            parent.ui.adjust_text_size.setValue(self.mode_settings[self.mode]['font_size'])
        elif self.mode == "audio_transcribe":
            current_file = self.mode_settings[self.mode]["current_editing_file"]

            if current_file:
                font_size = self.mode_settings[self.mode]["current_file"][current_file]['font_size']
                parent.ui.adjust_text_size.setValue(font_size)

    def handle_title_info(self, parent):
        app_name = parent.settings['app_name']

        try:
            if self.mode == "file_editing":
                current_file = self.mode_settings[self.mode]['current_file']
            elif self.mode == "audio_transcribe":
                current_file = self.mode_settings[self.mode]['current_editing_file']
            elif self.mode == "file_search":
                current_file = ""

            current_file = _retrieve_filename(current_file) if current_file else "Untitled"
        except KeyError:
            current_file = ""
        except TypeError:
            current_file = ""

        try:
            if self.mode == "file_editing":
                is_dirty = "x" if self.mode_settings[self.mode]['dirty_file'] else ""
            elif self.mode == "audio_transcribe":
                current_edit_file = self.mode_settings[self.mode]["current_editing_file"]
                is_dirty = "x" if self.mode_settings[self.mode]['current_file'][current_edit_file]["dirty_file"] else ""
            elif self.mode == "file_search":
                is_dirty = ""
        except KeyError:
            is_dirty = ""
        except TypeError:
            is_dirty = ""

        if self.mode == 'file_editing':
            mode = "Text Editor"
        elif self.mode == 'audio_transcribe':
            mode = "Audio Transcriber"
        elif self.mode == 'file_search':
            mode = "Search"
        else:
            mode = ""

        # if self.mode_settings[self.mode]['dirty_file']:
        description = f"""{app_name} - [{mode}] - {current_file} {is_dirty}"""
        parent.ui.titleRightInfo.setText(description)
