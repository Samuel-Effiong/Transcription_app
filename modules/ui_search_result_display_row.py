# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_result_display_rowfDKTVp.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *
from .resources_rc import *


class Ui_SearchResultDisplayRow(object):
    def setupUi(self, SearchResultDisplayRow):
        if SearchResultDisplayRow.objectName():
            SearchResultDisplayRow.setObjectName(u"SearchResultDisplayRow")
        SearchResultDisplayRow.resize(526, 494)
        SearchResultDisplayRow.setStyleSheet(u"QLineEdit {\n"
"	height: 24px;\n"
"	border-radius: 4px;\n"
"	background-color: white;\n"
"	border: 1px solid black\n"
"}")
        self.gridLayout = QGridLayout(SearchResultDisplayRow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.edit_button = QPushButton(SearchResultDisplayRow)
        self.edit_button.setObjectName(u"edit_button")

        self.gridLayout.addWidget(self.edit_button, 5, 0, 1, 1)

        self.row_teacher = QLineEdit(SearchResultDisplayRow)
        self.row_teacher.setObjectName(u"row_teacher")

        self.gridLayout.addWidget(self.row_teacher, 1, 1, 1, 2)

        self.row_theme = QLineEdit(SearchResultDisplayRow)
        self.row_theme.setObjectName(u"row_theme")

        self.gridLayout.addWidget(self.row_theme, 1, 4, 1, 2)

        self.row_date = QLabel(SearchResultDisplayRow)
        self.row_date.setObjectName(u"row_date")

        self.gridLayout.addWidget(self.row_date, 0, 4, 1, 2)

        self.row_message = QTextEdit(SearchResultDisplayRow)
        self.row_message.setObjectName(u"row_message")
        self.row_message.setStyleSheet(u"")

        self.gridLayout.addWidget(self.row_message, 3, 0, 1, 6)

        self.row_coordinator = QLineEdit(SearchResultDisplayRow)
        self.row_coordinator.setObjectName(u"row_coordinator")

        self.gridLayout.addWidget(self.row_coordinator, 0, 1, 1, 2)

        self.row_title = QLineEdit(SearchResultDisplayRow)
        self.row_title.setObjectName(u"row_title")

        self.gridLayout.addWidget(self.row_title, 2, 1, 1, 5)

        self.label_2 = QLabel(SearchResultDisplayRow)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ok_button = QPushButton(SearchResultDisplayRow)
        self.ok_button.setObjectName(u"ok_button")

        self.horizontalLayout.addWidget(self.ok_button)


        self.gridLayout.addLayout(self.horizontalLayout, 5, 5, 1, 1)

        self.label_5 = QLabel(SearchResultDisplayRow)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_3 = QLabel(SearchResultDisplayRow)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)

        self.label = QLabel(SearchResultDisplayRow)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_prev = QPushButton(SearchResultDisplayRow)
        self.search_prev.setObjectName(u"search_prev")
        self.search_prev.setMinimumSize(QSize(0, 22))
        self.search_prev.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_prev.setStyleSheet(u"border: none;\n"
"background-color: #BD92F4;\n"
"padding: 0 5px;")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_prev.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.search_prev)

        self.label_6 = QLabel(SearchResultDisplayRow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-weight: bold;\n"
"text-decoration: italics")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_7 = QLabel(SearchResultDisplayRow)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font-weight: bold;")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.search_next = QPushButton(SearchResultDisplayRow)
        self.search_next.setObjectName(u"search_next")
        self.search_next.setMinimumSize(QSize(0, 22))
        self.search_next.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_next.setStyleSheet(u"border: none;\n"
"background-color: #BD92F4;\n"
"padding: 0 5px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-arrow-circle-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_next.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.search_next)


        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 2, 1, 3)

        self.label_4 = QLabel(SearchResultDisplayRow)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)


        self.retranslateUi(SearchResultDisplayRow)

        QMetaObject.connectSlotsByName(SearchResultDisplayRow)
    # setupUi

    def retranslateUi(self, SearchResultDisplayRow):
        SearchResultDisplayRow.setWindowTitle(QCoreApplication.translate("SearchResultDisplayRow", u"Dialog", None))
        self.edit_button.setText(QCoreApplication.translate("SearchResultDisplayRow", u"Edit", None))
        self.row_date.setText("")
        self.label_2.setText(QCoreApplication.translate("SearchResultDisplayRow", u"Teacher:", None))
        self.ok_button.setText(QCoreApplication.translate("SearchResultDisplayRow", u"OK", None))
        self.label_5.setText(QCoreApplication.translate("SearchResultDisplayRow", u"Title:", None))
        self.label_3.setText(QCoreApplication.translate("SearchResultDisplayRow", u"Theme:", None))
        self.label.setText(QCoreApplication.translate("SearchResultDisplayRow", u"Coordinator:", None))
        self.search_prev.setText("")
        self.label_6.setText(QCoreApplication.translate("SearchResultDisplayRow", u"prev", None))
        self.label_7.setText(QCoreApplication.translate("SearchResultDisplayRow", u"next", None))
        self.search_next.setText("")
        self.label_4.setText(QCoreApplication.translate("SearchResultDisplayRow", u"Date:", None))
    # retranslateUi

