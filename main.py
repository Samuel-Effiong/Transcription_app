
import sys
import os
import platform


# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////

from modules import *
from widgets import *
from search_engine import SearchInterface

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()

        self.signals = Signals()
        self.custom_ui_function = Files()
        self.search_interface = SearchInterface(self.custom_ui_function)

        self.ui.setupUi(self)

        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        UIFunctions.settings['enable_custom_title_bar'] = True
        self.settings = Settings_Json().items

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = self.settings['app_name']
        description = f"{self.settings['app_name']} - [Text Editor]"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)
        UIFunctions.set_current_date(self)
        UIFunctions.add_editor_settings_widgets(self)
        UIFunctions.add_search_widgets(self)
        UIFunctions.add_transcribed_widgets(self)
        UIFunctions.toggle_internet_connection_display(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_open_file.clicked.connect(self.buttonClick)
        widgets.btn_new_file.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.btn_search.clicked.connect(self.buttonClick)
        widgets.btn_transcribe.clicked.connect(self.buttonClick)

        # widgets.btn_widgets.clicked.connect(self.buttonClick)

        self.customWidgetSignals()
        self.addButtonActions()

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        self.setMouseTracking(True)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = True
        themeFile = self.settings['theme']

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

        # set the focus
        widgets.text_editor.setFocus()

        self.ui.transcription_progressBar_2.setHidden(True)
        self.ui.loading_files_widget.setHidden(True)
        self.ui.warning_display.setHidden(True)
        self.custom_ui_function.toggle_additional_information_frame(self)
        self.search_interface.toggle_additional_filter_frame(self)

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

            self.ui.titleRightInfo.setText(f"{self.settings['app_name']} - [Text Editor]")
            self.custom_ui_function.file_operations.mode = 'file_editing'
            self.custom_ui_function.file_operations.mode_settings['mode_memory'] = self.custom_ui_function.file_operations.mode

        # OPEN FILE
        elif btnName == "btn_open_file":
            self.custom_ui_function.open(self)

        # SHOW NEW PAGE
        elif btnName == "btn_new_file":
            print("love GOD")
            widgets.btn_home.click()
            self.custom_ui_function.file_operations.mode = 'file_editing'
            self.custom_ui_function.file_operations.mode_settings['mode_memory'] = self.custom_ui_function.file_operations.mode
            self.custom_ui_function.new(self)

        elif btnName == "btn_save":
            if self.custom_ui_function.file_operations.mode != 'file_search':
                self.custom_ui_function.save(self)
                print("Save BTN clicked!")

        # SHOW SEARCH PAGE
        elif btnName == "btn_search":
            widgets.stackedWidget.setCurrentWidget(widgets.search)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

            self.custom_ui_function.file_operations.mode = 'file_search'
            self.custom_ui_function.file_operations.mode_settings['mode_memory'] = self.custom_ui_function.file_operations.mode
            self.custom_ui_function.toggle_dirty_state(dirty=False, parent=self)

        elif btnName == "btn_transcribe":
            widgets.stackedWidget.setCurrentWidget(widgets.transcribe)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

            # UIFunctions.display_experimental_warning(self)
            self.custom_ui_function.file_operations.mode = 'audio_transcribe'
            self.custom_ui_function.file_operations.mode_settings['mode_memory'] = self.custom_ui_function.file_operations.mode

            self.custom_ui_function.toggle_dirty_state(
                parent=self,
                dirty=self.custom_ui_function.file_operations.mode_settings[
                    self.custom_ui_function.file_operations.mode]['dirty_file'])

        if btnName in ['btn_home', 'btn_new_file']:
            # FIXME: solution patches, not good
            # if self.custom_ui_function.file_operations.mode in ['file_search', 'audio_transcribe']:
            #     return
            self.custom_ui_function.file_operations.mode = 'file_editing'
            self.custom_ui_function.file_operations.mode_settings['mode_memory'] = self.custom_ui_function.file_operations.mode

            if self.custom_ui_function.file_operations.mode_settings[
                self.custom_ui_function.file_operations.mode]['current_file']:

                self.custom_ui_function.toggle_dirty_state(parent=self,
                                                           dirty=self.custom_ui_function.file_operations.mode_settings[
                                                               self.custom_ui_function.file_operations.mode]['dirty_file'])

        self.custom_ui_function.file_operations.restore_mode_settings(self)

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def addButtonActions(self):
        save_action = self.create_actions("Save", QKeySequence.Save, lambda: self.custom_ui_function.save(self))
        open_action = self.create_actions("Open", QKeySequence.Open,
                                          lambda: self.custom_ui_function.open(self))
        new_action = self.create_actions("New", QKeySequence.New, lambda: self.custom_ui_function.new(self))

        self.ui.btn_save.addAction(save_action)
        self.ui.btn_open_file.addAction(open_action)
        self.ui.btn_new_file.addAction(new_action)

    def create_actions(self, label, shortcut=None, slot=None):
        """Create the action of a menu using the given parameter and returns the action object"""
        action = QAction(label, self)
        if shortcut:
            action.setShortcut(shortcut)
        if slot:
            action.triggered.connect(slot)

        return action
    
    def __text_custom_widget_signals(self):
        # text editor signals
        self.ui.text_editor.textChanged.connect(lambda: self.custom_ui_function.detect_text_changed(self))
        self.ui.adjust_text_size.valueChanged.connect(lambda: self.custom_ui_function.adjust_editor_font_size(self))
        self.ui.date_edit.clicked.connect(lambda: self.custom_ui_function.select_date(self, mode='text'))
        self.ui.btn_font.clicked.connect(lambda: self.custom_ui_function.select_font(self))
        
        self.ui.categories_combobox.currentTextChanged.connect(lambda: self.custom_ui_function.text_control.confirm_unique_identifier(self))
        self.ui.text_unique_identifier_line_edit.textChanged.connect(lambda: self.custom_ui_function.text_control.confirm_unique_identifier(self))
        self.ui.show_additional_information_frame_push_button.clicked.connect(lambda: self.custom_ui_function.toggle_additional_information_frame(self))
        self.ui.teacher_name_line_edit.textChanged.connect(lambda: self.custom_ui_function.text_control.text_validators.ensure_teacher_name_is_not_empty(self))
        self.ui.coordinator_name_line_edit.textChanged.connect(lambda: self.custom_ui_function.text_control.text_validators.ensure_coordinator_name_is_not_empty(self))
    
    def __transcription_custom_widget_signals(self):
        # audio transcribe signals
        self.ui.select_audio_button.clicked.connect(lambda: self.custom_ui_function.open(self))
        self.ui.transcribe_date_edit.clicked.connect(lambda: self.custom_ui_function.select_date(self, mode='transcribe'))
        self.ui.start_transcription_button.clicked.connect(lambda: self.custom_ui_function.transcribe_audio(self))
        self.ui.transcribe_file_list.currentTextChanged.connect(lambda: self.custom_ui_function.display_list_widget_info(self))
        self.ui.transcribe_file_list.doubleClicked.connect(lambda: self.custom_ui_function.edit_transcribed_text(self))
        self.signals.transcription_completion_signal.connect(lambda fname: self.custom_ui_function.display_list_widget_info(self))
        self.signals.transcription_completion_signal.connect(lambda fname: self.custom_ui_function.display_transcription_progress(self))
        self.signals.progress_signal.connect(lambda: self.custom_ui_function.display_list_widget_info(self))
        self.ui.continue_transcription.clicked.connect(lambda: self.custom_ui_function.transcribe_engine.pause_resume_transcription(self))
        
    def __search_custom_widget_signals(self):
        # search interface signals
        self.ui.back_to_search_home.clicked.connect(self.ui.btn_search.click)
        self.ui.search_pushButton.clicked.connect(lambda: self.search_interface.show_search_result(self))
        self.ui.search_push_button_small.clicked.connect(lambda: self.search_interface.show_search_result(self, area='small'))
        self.ui.year_category.currentTextChanged.connect(lambda: self.search_interface.update_search_result(self))
        self.ui.month_category.currentTextChanged.connect(lambda: self.search_interface.update_search_result(self))
        self.ui.days_category.currentTextChanged.connect(lambda: self.search_interface.update_search_result(self))
        self.ui.coordinator_combobox.currentTextChanged.connect(lambda: self.search_interface.update_search_result(self))
        self.ui.teacher_combobox.currentTextChanged.connect(lambda: self.search_interface.update_search_result(self))
        self.ui.advanced_search_filter_pushbutton.clicked.connect(lambda: self.search_interface.toggle_additional_filter_frame(self))
        
        self.ui.search_result_display.doubleClicked.connect(lambda: self.search_interface.display_row_information(self))

    def customWidgetSignals(self):
        print("Text changed")
        self.__text_custom_widget_signals()
        self.__transcription_custom_widget_signals()
        self.__search_custom_widget_signals()
        
    def enterEvent(self, *args, **kwargs):
        self.custom_ui_function.file_operations.mode = self.custom_ui_function.file_operations.mode_settings['mode_memory']

    def closeEvent(self, *args, **kwargs):
        confirmation = QMessageBox().warning(self, "Confirm Exit", "Are you sure you want to exit?",
                                             QMessageBox.Ok | QMessageBox.Cancel)

        if confirmation == QMessageBox.Ok:
            self.custom_ui_function.transcribe_engine.threadpool().clear()
            self.custom_ui_function.database.close_db()
        else:
            event = args[0]
            event.ignore()
            return
        print("Love you God")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = SplashScreen(main_window=MainWindow)
    try:
        sys.exit(app.exec_())
    except BaseException as e:
        pass
