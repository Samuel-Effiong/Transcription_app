
import re
from qt_core import *
from .ui_search_result_display_row import Ui_SearchResultDisplayRow


class SearchResultDisplayRow(QDialog):
    def __init__(self, main_window, search_query, columns_data, *, additional_param):
        super(SearchResultDisplayRow, self).__init__()

        self.search_query = search_query
        self.main_window = main_window
        self.columns_data = columns_data
        self.additional_param = additional_param

        self.ui = Ui_SearchResultDisplayRow()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.populate_dialog()
        self.set_the_selected_text_background()
        self.search_all_occurrence_of_search_query()
        
        self.cursor = self.ui.row_message.textCursor()
        self.highlight_all_occurence_of_search_query(self.cursor)
        
        self.current_active_highlighted_cursor = 0

        # connect slot to signal
        self.ui.ok_button.clicked.connect(self.close_dialog)
        self.ui.search_prev.clicked.connect(lambda: self.find('prev'))
        self.ui.search_next.clicked.connect(lambda: self.find('next'))
        
    def set_the_selected_text_background(self):
        self.text_format = QTextCharFormat()
        self.text_format.setBackground(QBrush(QColor('blue')))
        self.text_format.setForeground(QBrush(QColor('white')))
        
        self.active_text_format = QTextCharFormat()
        self.active_text_format.setBackground(QBrush(QColor('blue')))
        self.active_text_format.setForeground(QBrush(QColor('white')))

    def close_dialog(self):
        self.accept()

    def populate_dialog(self):
        self.ui.row_title.setText(self.columns_data['Titles'])
        self.ui.row_theme.setText(self.columns_data['Themes'])
        self.ui.row_teacher.setText(self.columns_data['Teachers'])
        self.ui.row_coordinator.setText(self.columns_data['Coordinators'])
        self.ui.row_message.setText(self.columns_data['Messages'])
        self.ui.row_date.setText(self.columns_data['Dates'].toString())

        self.setWindowTitle(self.columns_data['Id'])
        
    def search_all_occurrence_of_search_query(self):
        query = self.preprocess_query()
        pattern = re.compile(pattern=query, flags=re.IGNORECASE)
        
        self.search_query_occurence = list(pattern.finditer(self.ui.row_message.toPlainText()))
        
    def highlight_all_occurence_of_search_query(self, cursor):
        for match in self.search_query_occurence:
            start, end = match.start(), match.end()
            self.cursor.setPosition(start, QTextCursor.MoveAnchor)
            self.cursor.setPosition(end, QTextCursor.KeepAnchor)
            self.cursor.mergeCharFormat(self.text_format)
        
    def preprocess_query(self) -> str:
        query = "|".join([f"({word})" for word in self.search_query])
        return query
    
    def highlight_active_query(self, match):
        start, end = match.start(), match.end()
        
        self.cursor.setPosition(start, QTextCursor.MoveAnchor) 
        self.cursor.setPosition(end, QTextCursor.KeepAnchor)
        # self.cursor.mergeCharFormat(self.active_text_format)
        
        # adjust the scrollbar to where the text is 
        self.ui.row_message.ensureCursorVisible()
        self.ui.row_message.setTextCursor(self.cursor)

    def find(self, method='next'):
        if method == 'next':
            self.current_active_highlighted_cursor += 1
        elif method == 'prev':
            self.current_active_highlighted_cursor -= 1
            
        try:
            match = self.search_query_occurence[self.current_active_highlighted_cursor]
        except IndexError:
            if method == 'next':
                self.current_active_highlighted_cursor = 0
            elif method == 'prev':
                self.current_active_highlighted_cursor = len(self.search_query_occurence) - 1
            match = self.search_query_occurence[self.current_active_highlighted_cursor]
            
        self.highlight_active_query(match)
        
    def disable_widgets(self):
        self.ui.row_message.setDisabled(True)
        self.ui.row_coordinator.setDisabled(True)
        self.ui.row_date.setDisabled(True)
        self.ui.row_teacher.setDisabled(True)
        self.ui.row_theme.setDisabled(True)
        self.ui.row_title.setDisabled(True)

    def edit_row(self):
        pass


