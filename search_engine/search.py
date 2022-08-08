
from qt_core import *

from .keyword_search import KeywordSearch
from .semantic_search import SemanticSearch

from PyQt5.QtSql import QSqlQuery
from modules.display_search_row import SearchResultDisplayRow


class SearchInterface:
    def __init__(self, file_control):
        self.__file_control = file_control
        self.__keyword_search = KeywordSearch(self.__file_control)
        self.__semantic_search = SemanticSearch(self.__file_control)

        self.search_query = None
        self.keyword = None
        self.semantic = None

    def __update_display_widget(self, *, response, parent):
        parent.ui.search_result_display.setModel(self.__file_control.database.model)

        if response:
            self.__file_control.database.model.setFilter(response)
            idx = self.__file_control.database.model.fieldIndex("Topic Vectors")
            self.__file_control.database.model.removeColumns(idx, 1)
        else:
            query = QSqlQuery("""SELECT * FROM "Sermons" """, self.__file_control.database.db)
            self.__file_control.database.model.setQuery(query)

    def handle_teacher_category(self, parent):
        query = """SELECT DISTINCT("Teachers") FROM "Sermons" """
        responses = self.__file_control.database.raw_query(query, 1)

        teachers = [row[0] if row[0] else 'None' for row in responses]
        if 'None' not in teachers:
            teachers.insert(0, 'None')
        parent.ui.teacher_combobox.clear()
        parent.ui.teacher_combobox.addItems(teachers)

    def handle_coordinator_category(self, parent):
        query = """SELECT DISTINCT("Coordinators") FROM "Sermons" """
        responses = self.__file_control.database.raw_query(query, 1)

        coordinators = [row[0] if row[0] else 'None' for row in responses]
        if 'None' not in coordinators:
            coordinators.insert(0, 'None')
        parent.ui.coordinator_combobox.clear()
        parent.ui.coordinator_combobox.addItems(coordinators)

    def show_search_result(self, parent, *, area=None):
        self.keyword: bool = parent.ui.keyword_checkbox.isChecked()
        self.semantic: bool = parent.ui.semantic_checkbox.isChecked()

        # reset the  previous search additional params
        parent.ui.year_category.setCurrentIndex(0)
        parent.ui.month_category.setCurrentIndex(0)
        parent.ui.days_category.setCurrentIndex(0)
        parent.ui.teacher_combobox.setCurrentIndex(0)
        parent.ui.coordinator_combobox.setCurrentIndex(0)

        if not area:
            self.search_query = parent.ui.search_line_edit.text().strip()
        else:
            self.search_query = parent.ui.search_line_edit_small.text().strip()

        if self.keyword and self.semantic:
            keyword_response = self.__keyword_search.search(self.search_query)
            semantic_response = self.__semantic_search.search(self.search_query)

            responses = f"({keyword_response} OR {semantic_response})"

        elif self.keyword:
            responses = self.__keyword_search.search(self.search_query)
            if not area:
                parent.ui.search_line_edit_small.setPlaceholderText("Enter your search keywords")
        elif self.semantic:
            responses = self.__semantic_search.search(self.search_query)
            if not area:
                parent.ui.search_line_edit_small.setPlaceholderText("Enter your search phrase")

        self.__update_display_widget(response=responses, parent=parent)
        parent.ui.stackedWidget.setCurrentWidget(parent.ui.search_result)

        self.handle_teacher_category(parent)
        self.handle_coordinator_category(parent)

    def update_search_result(self, parent):
        coordinator = parent.ui.coordinator_combobox.currentText()
        teacher = parent.ui.teacher_combobox.currentText()

        year = parent.ui.year_category.currentText()
        month = parent.ui.month_category.currentText()
        day = parent.ui.days_category.currentText()

        additional_param = {
            "coordinator": coordinator,
            "teacher": teacher,
            "year": year,
            "month": month,
            "day": day
        }

        if self.keyword and self.semantic:
            keyword_response = self.__keyword_search.search(self.search_query)
            semantic_response = self.__semantic_search.search(self.search_query)

            responses = f"({keyword_response} OR {semantic_response})"
        elif self.keyword:
            responses = self.__keyword_search.search(self.search_query, additional_param=additional_param)
        elif self.semantic:
            responses = self.__semantic_search.search(self.search_query, additional_param=additional_param)

        self.__update_display_widget(response=responses, parent=parent)

    def toggle_additional_filter_frame(self, parent):
        value = parent.ui.additional_filter_frame.isHidden()
        if not value:
            icon = QIcon(u":/icons/images/icons/cil-arrow-circle-left.png")
        else:
            icon = QIcon(u":/icons/images/icons/cil-arrow-circle-right.png")

        parent.ui.advanced_search_filter_pushbutton.setIcon(icon)
        parent.ui.additional_filter_frame.setHidden(not value)

    def display_row_information(self, parent):
        current_row = parent.ui.search_result_display.currentIndex().row()

        columns_data = {self.__file_control.database.model.record().fieldName(column): self.__file_control.database.model.index(current_row, column).data()
                   for column in range(parent.ui.search_result_display.model().columnCount())}
        
        if self.keyword and self.semantic:
            keyword_query = self.__keyword_search.preprocess_query(self.search_query)
            semantic_query = self.__semantic_search.get_similar_texts
            semantic_query.extend(keyword_query)
            
            query = semantic_query
            
        elif self.keyword:
            query = self.__keyword_search.preprocess_query(self.search_query)
        elif self.semantic:
            query = self.__semantic_search.get_similar_texts
            
        additional_param = {
            'method': 'both' if self.keyword and self.semantic else 'semantic' if self.semantic else 'keyword'
        }

        display_interface = SearchResultDisplayRow(parent, query, columns_data, additional_param=additional_param)

        if display_interface.exec_():
            print("Love")

        pass
