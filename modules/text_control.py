
import re
import string
from qt_core import *


class _TextValidators:
    def __init__(self, file_control):
        self.file_control = file_control
        self.__validator_score = {
            'isIdValid': True,
            'isMessageValid': False,
            'isCoordinatorNameValid': False,
            'isTeacherNameValid': False
        }

        self.error_style_sheet = "border: 2px solid red;"
        self.valid_style_sheet = "border: 1px solid black;"

    @property
    def validator_score(self) -> dict:
        return self.__validator_score

    def __display_errors_warning_in_precedence(self, parent):
        category = parent.ui.categories_combobox.currentText()
        if not self.__validator_score['isIdValid']:
            id_ = self.file_control.file_operations.mode_settings['file_editing']['current_file']
            warning_text = f"Warning: {id_} already exist in {category} database! Saving will " \
                           f"overwrite it"
            parent.ui.warning_display.setText(warning_text)
            parent.ui.warning_display.setHidden(False)
        elif not self.__validator_score["isMessageValid"]:
            parent.ui.warning_display.setText(f"Can't save {category} without message")
            parent.ui.warning_display.setHidden(False)
        elif not self.__validator_score["isTeacherNameValid"]:
            parent.ui.warning_display.setText("Name of Teacher can't be empty!")
            parent.ui.warning_display.setHidden(False)
        elif not self.__validator_score["isCoordinatorNameValid"]:
            parent.ui.warning_display.setText("Name of Service coordinator can't be empty")
            parent.ui.warning_display.setHidden(False)
        else:
            parent.ui.warning_display.setHidden(True)

    def ensure_message_text_is_not_empty(self, parent):
        text = parent.ui.text_editor.toPlainText().strip()
        category = parent.ui.categories_combobox.currentText()

        if not text:  # if empty
            parent.ui.warning_display.setText(f"Can't save {category} without message")
            parent.ui.warning_display.setHidden(False)
            parent.ui.text_editor.setStyleSheet(self.error_style_sheet)
            self.__validator_score["isMessageValid"] = False
        else:
            parent.ui.text_editor.setStyleSheet(self.valid_style_sheet)
            self.__validator_score["isMessageValid"] = True
            self.__display_errors_warning_in_precedence(parent)

    def ensure_coordinator_name_is_not_empty(self, parent):
        text = parent.ui.coordinator_name_line_edit.text().strip()

        if not text:
            parent.ui.warning_display.setText(f"Name of Service coordinator can't be empty!")
            parent.ui.warning_display.setHidden(False)
            parent.ui.coordinator_name_line_edit.setStyleSheet(self.error_style_sheet)
            self.__validator_score["isCoordinatorNameValid"] = False
        else:
            parent.ui.coordinator_name_line_edit.setStyleSheet(self.valid_style_sheet)
            self.__validator_score["isCoordinatorNameValid"] = True
            self.__display_errors_warning_in_precedence(parent)

    def ensure_teacher_name_is_not_empty(self, parent):
        text = parent.ui.teacher_name_line_edit.text().strip()

        if not text:
            parent.ui.warning_display.setText(f"Name of Teacher can't be empty!")
            parent.ui.warning_display.setHidden(False)
            parent.ui.teacher_name_line_edit.setStyleSheet(self.error_style_sheet)
            self.__validator_score["isTeacherNameValid"] = False
        else:
            parent.ui.teacher_name_line_edit.setStyleSheet(self.valid_style_sheet)
            self.__validator_score["isTeacherNameValid"] = True
            self.__display_errors_warning_in_precedence(parent)


class TextControl:
    def __init__(self, file_control):
        self.file_control = file_control
        self.text_validators = _TextValidators(file_control)

    def open_text_file(self, parent):
        # if the user has selected an text from a folder, open the file dialog box
        # to that previous opened folder path
        if self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['dirty_file']:
            message = "Do you want to save the changes made to this document?\n"
            message += "Your changes will be lost if you don't save them"

            reply = self.file_control.raise_saving_message(parent, message=message)

            if reply == QMessageBox.Save:
                self.file_control.save(parent)
            elif reply == QMessageBox.Cancel:
                return

        filename, _ = QFileDialog().getOpenFileName(
            parent, 'Select file',
            f"""{self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['previous_file']
            if self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['previous_file'] else '.'}""",
            "text files (*.txt);;")

        if filename and os.path.exists(filename):
            print(filename)
            # try different encodings
            try:
                self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['file_encoding'] = 'utf8'
                with open(filename, encoding=self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['file_encoding']) as file:
                    text = file.read()
            except UnicodeDecodeError:
                try:
                    self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['file_encoding'] = 'utf32'
                    with open(filename,
                              encoding=self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['file_encoding']) as file:
                        text = file.read()
                except UnicodeDecodeError:
                    try:
                        self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['file_encoding'] = 'utf16'
                        with open(filename,
                                  encoding=self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['file_encoding']) as file:
                            text = file.read()
                    except Exception:
                        # Finally raise a warning if file can't be opened
                        message = "Unable to read file, file may be corrupted"
                        QMessageBox.warning(parent, "File error", message, QMessageBox.Ok)
                        return
                pass

            try:
                pattern = re.compile("<h1>.+</h1>")
                heading = pattern.match(text).group()
                heading = re.sub("<.?[a-z0-9]{2}>", "", heading)
                text = pattern.sub("", text).strip()
            except AttributeError:
                heading = ""
            parent.ui.heading_line_edit.setText(heading)
            parent.ui.text_editor.setPlainText(text)
            self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['previous_file'] = filename
            self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['current_file'] = filename

    @staticmethod
    def __format_save_confirmation_message(confirmation, category):
        if confirmation:
            message = '<span style="font-style: italic">{}</span>'
            confirmation = '<span style="color: #00FF00; font-weight=bold; font-size=14px">{}</span>'

            message = message.format(f"{category} update {confirmation.format('Successful')}")
        else:
            message = '<span style="font-style: italic">{}</span>'
            confirmation = '<span style="color: red">{}</span>'

            message = message.format(f"{category} update {confirmation.format('Failed')}")

        return message

    def save_text(self, parent):
        # # SAVE TO DATABASE
        current_file = self.file_control.file_operations.mode_settings['file_editing']['current_file']
        if current_file is None:
            self.confirm_unique_identifier(parent)
            current_file = self.file_control.file_operations.mode_settings['file_editing']['current_file']

            if current_file is None:
                raise ValueError("Current File can't be None")

            if parent.ui.warning_display.isVisible():
                message = "This transcripts already exists in the database!\n"
                message += "Continuing in this action will overwrite them, \n\n" \
                           "Do you still want to go on?"

                reply = self.file_control.raise_saving_message(parent, message=message)

                if reply == QMessage.Cancel:
                    return

        if current_file:
            id_valid = self.text_validators.validator_score["isIdValid"]
            message_valid = self.text_validators.validator_score["isMessageValid"]
            teacher_name_valid = self.text_validators.validator_score["isTeacherNameValid"]
            coordinator_name_valid = self.text_validators.validator_score["isCoordinatorNameValid"]

            if id_valid and message_valid and teacher_name_valid and coordinator_name_valid:
                # retrieve a list of all the titles present
                category = parent.ui.categories_combobox.currentText()

                responses = self.file_control.database.retrieve_data_from_database(
                    "Id", table_category=category, Id=current_file)

                title = parent.ui.heading_line_edit.text()
                message = parent.ui.text_editor.toPlainText()
                date = parent.ui.text_unique_identifier.text().strip()
                date = QDate.fromString(date, f"GLH-ddd d MMM, yyyy-").toPyDate()
                teacher = " ".join([word.capitalize() for word in parent.ui.teacher_name_line_edit.text().strip().split()])
                theme = parent.ui.theme_name_line_edit.text().strip()
                coordinator = " ".join([word.capitalize() for word in parent.ui.coordinator_name_line_edit.text().strip().split()])

                if responses:
                    # Update
                    
                    # get the topic vector of the message
                    
                    
                    # FIXME: Include regenerated automatic summarised text
                    # TODO: update the topic vectors in the database
                    confirmation = self.file_control.database.update_data_in_database(
                        table_category=category, conditions={'Id': current_file},
                        Messages=message, Titles=title, Teachers=teacher,
                        Themes=theme, Coordinators=coordinator
                    )

                    message = self.__format_save_confirmation_message(confirmation, category)
                else:
                    # TODO: Include the topic vectors in the database                    
                    confirmation = self.file_control.database.insert_data_in_database(
                        table_category=category, Messages=message, Teachers="Pst Ita Udoh",
                        Dates=date, Id=current_file, Titles=title, Themes=theme,
                        Coordinators=coordinator
                    )

                    message = self.__format_save_confirmation_message(confirmation, category)
                parent.ui.version.setText(message)
                QTimer.singleShot(3000, parent.ui.version.clear)
                parent.ui.warning_display.setHidden(True)
                self.file_control.file_operations.mode_settings['file_editing']['dirty_file'] = False
            else:
                self.text_validators.ensure_message_text_is_not_empty(parent)
        # SAVE TO FILE DIRECTORIES
        # if self.current_file is None:  # open a save as dialog
        # if self.file_operations.mode == 'file_editing':

        # if self.file_control.file_operations.mode != 'file_search' and self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['current_file'] is None:
        #     filename, _ = QFileDialog().getSaveFileName(parent, "Save Text", ".",
        #                                                 "text files (*.txt);;")
        #
        #     print(filename)
        #     if filename:
        #         self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['current_file'] = filename
        #         self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['file_encoding'] = 'utf8'
        #
        # if self.file_control.file_operations.mode != 'file_search' and self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['current_file']:
        #     try:
        #         with open(self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['current_file'], "w",
        #                   encoding=self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode][
        #                       'file_encoding']) as file:
        #             topic = parent.ui.heading_line_edit.text()
        #             text = parent.ui.text_editor.toPlainText()
        #
        #             text = f"<h1>{topic}</h1>\n{text}"
        #             file.write(text)
        #     except Exception:
        #         os.remove(self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['current_file'])
        #
        #     self.file_control.toggle_dirty_state(dirty=False, parent=parent)

    def new(self, parent):
        # TODO: Open new file in a new window
        if self.file_control.file_operations.mode == 'file_editing':
            if self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['dirty_file']:
                message = "Do you want to save the changes made to this document?\n"
                message += "Your changes will be lost if you don't save them"
                reply = self.file_control.raise_saving_message(parent, message=message)

                if reply == QMessageBox.Save:
                    self.file_control.save(parent)
                elif reply == QMessageBox.Cancel:
                    return

                if self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['current_file'] or reply == QMessageBox.Discard:
                    self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['current_file'] = None
                    self.file_control.file_operations.mode_settings[self.file_control.file_operations.mode]['file_encoding'] = None

            parent.ui.coordinator_name_line_edit.clear()
            parent.ui.teacher_name_line_edit.clear()
            parent.ui.theme_name_line_edit.clear()
            parent.ui.text_unique_identifier_line_edit.clear()
            parent.ui.heading_line_edit.clear()
            parent.ui.text_editor.clear()
            self.file_control.toggle_dirty_state(dirty=True, parent=parent)

    def confirm_unique_identifier(self, parent):
        first_part = parent.ui.text_unique_identifier.text().strip()
        second_part = parent.ui.text_unique_identifier_line_edit.text().strip()
        if second_part and not second_part.isupper() and not second_part.isnumeric():
            second_part = second_part.upper()
            second_part = re.sub(f"[{string.punctuation}]", "", second_part)
            parent.ui.text_unique_identifier_line_edit.setText(second_part)
            return

        id_ = f"{first_part}{second_part}"
        parsed_date = QDate.fromString(id_, f"GLH-ddd d MMM, yyyy-{second_part}")

        id_ = f"{parsed_date.toString('GLH-ddd')}{parsed_date.toString('dMMyyyy')}-{second_part}"

        if not second_part:
            id_ = id_.rstrip("-")

        category = parent.ui.categories_combobox.currentText()
        response = self.file_control.database.retrieve_data_from_database(
            "Id", table_category=category, Id=id_
        )

        if response:
            warning_text = f"Warning: {id_} already exist in {category} database! Saving will " \
                           f"overwrite it"
            parent.ui.warning_display.setText(warning_text)
            parent.ui.warning_display.setHidden(False)
            self.text_validators.validator_score["isIdValid"] = False
        else:
            parent.ui.warning_display.setHidden(True)
            self.text_validators.validator_score["isIdValid"] = True

        self.file_control.file_operations.mode_settings['file_editing']['current_file'] = id_
        self.file_control.file_operations.handle_title_info(parent)

