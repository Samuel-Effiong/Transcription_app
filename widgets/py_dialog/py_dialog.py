import os.path

from qt_core import *


class PyDialog(QDialog):
    def __init__(self, parent, ui, *, fname_abs_path):
        super(PyDialog, self).__init__(parent)
        self.__parent = parent
        self.ui = ui
        self.ui.setupUi(self)

        self.fname_abs_path = fname_abs_path
        self.file_operations = parent.custom_ui_function.file_operations

        save_action = self.__parent.create_actions("Save", QKeySequence.Save, lambda: self.__save_audio())
        find_action = self.__parent.create_actions("Find..", QKeySequence.Find, lambda: print("Find in page..."))

        self.addActions([save_action, find_action])

        self.ui.edit_transcribed_text_edit.textChanged.connect(lambda: self.refresh())
        self.ui.save_transcript_btn.clicked.connect(lambda: self.__save_audio())
        self.ui.close_transcript_dialog.clicked.connect(self.close)

    def enterEvent(self, *args, **kwargs) -> None:
        if self.isActiveWindow():
            print("Dialog space")
        self.file_operations.mode = "audio_transcribe"
        self.file_operations.mode_settings[self.file_operations.mode]['current_editing_file'] = self.fname_abs_path

    def __save_audio(self):
        message = "You must transcribe an audio first, before you can save!"
        if not self.file_operations.mode_settings[self.file_operations.mode]['is_transcribed']:
            QMessageBox.warning(self.__parent, "Unable to Save", message)
            return

        file, ext = os.path.splitext(self.fname_abs_path)
        if not self.file_operations.mode_settings[self.file_operations.mode]['current_file'][self.fname_abs_path][
            'txt_format_path']:
            # if self.file_operations.mode_settings[self.file_operations.mode]['current_editing_file'] is None:
            filename, _ = QFileDialog().getSaveFileName(self.__parent, "Save Transcribed audio", f"{file}.txt",
                                                        "text file (*.txt);;")
            if filename:
                self.file_operations.mode_settings[self.file_operations.mode]['current_file'][self.fname_abs_path][
                    'txt_format_path'] = filename

        if self.file_operations.mode_settings[self.file_operations.mode]['current_file'][self.fname_abs_path][
            'txt_format_path']:
            text = self.file_operations.mode_settings[self.file_operations.mode]['current_file'][self.fname_abs_path][
                'text']
            try:
                with open(self.file_operations.mode_settings[self.file_operations.mode]['current_file'][
                              self.fname_abs_path][
                              'txt_format_path'], mode="w", encoding='utf8') as file:
                    file.write(text)
            except Exception as e:
                print(e)
                os.remove(
                    self.file_operations.mode_settings[self.file_operations.mode]['current_file'][self.fname_abs_path][
                        'txt_format_path'])
            self.toggle_dirty_state(dirty=False)

    def refresh(self):
        text = self.ui.edit_transcribed_text_edit.toPlainText()
        self.file_operations.mode_settings[self.file_operations.mode]['current_file'][self.fname_abs_path][
            'text'] = text

        self.file_operations.mode = 'audio_transcribe'
        self.file_operations.mode_settings[self.file_operations.mode]['current_editing_file'] = self.fname_abs_path

        self.toggle_dirty_state(dirty=True)

    def toggle_dirty_state(self, *, dirty):
        self.file_operations.mode_settings[self.file_operations.mode]['current_file'][self.fname_abs_path][
            'dirty_file'] = dirty

        self.handle_title_info()

    def handle_title_info(self):
        is_dirty = "x" if \
        self.file_operations.mode_settings[self.file_operations.mode]['current_file'][self.fname_abs_path][
            "dirty_file"] else ""

        fname = os.path.basename(self.fname_abs_path)
        fname, _ = os.path.splitext(fname)
        fname = f"{fname}.txt"
        description = f"""{os.path.basename(self.fname_abs_path)} {is_dirty}"""
        self.setWindowTitle(description)
