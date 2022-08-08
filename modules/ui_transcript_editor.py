# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transcript_editorfWCkwx.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *
from .resources_rc import *


class Ui_TranscribeEditor(object):
    def setupUi(self, TranscribeEditor):
        if TranscribeEditor.objectName():
            TranscribeEditor.setObjectName(u"TranscribeEditor")
        TranscribeEditor.resize(500, 469)
        TranscribeEditor.setStyleSheet(u"color: white;")
        self.gridLayout = QGridLayout(TranscribeEditor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.edit_transcribed_text_edit = QTextEdit(TranscribeEditor)
        self.edit_transcribed_text_edit.setObjectName(u"edit_transcribed_text_edit")
        self.edit_transcribed_text_edit.setEnabled(True)
        self.edit_transcribed_text_edit.setMinimumSize(QSize(200, 200))
        self.edit_transcribed_text_edit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.edit_transcribed_text_edit, 2, 0, 1, 3)

        self.save_transcript_btn = QPushButton(TranscribeEditor)
        self.save_transcript_btn.setObjectName(u"save_transcript_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_transcript_btn.sizePolicy().hasHeightForWidth())
        self.save_transcript_btn.setSizePolicy(sizePolicy)
        self.save_transcript_btn.setMinimumSize(QSize(100, 30))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.save_transcript_btn.setFont(font)
        self.save_transcript_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_transcript_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"padding: 0 10px;")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.On)
        self.save_transcript_btn.setIcon(icon)

        self.gridLayout.addWidget(self.save_transcript_btn, 1, 0, 1, 1)

        self.close_transcript_dialog = QPushButton(TranscribeEditor)
        self.close_transcript_dialog.setObjectName(u"close_transcript_dialog")
        sizePolicy.setHeightForWidth(self.close_transcript_dialog.sizePolicy().hasHeightForWidth())
        self.close_transcript_dialog.setSizePolicy(sizePolicy)
        self.close_transcript_dialog.setMinimumSize(QSize(100, 30))
        self.close_transcript_dialog.setFont(font)
        self.close_transcript_dialog.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_transcript_dialog.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"padding: 0 10px;")

        self.gridLayout.addWidget(self.close_transcript_dialog, 3, 2, 1, 1)

        self.find_in_transcript_btn = QPushButton(TranscribeEditor)
        self.find_in_transcript_btn.setObjectName(u"find_in_transcript_btn")
        sizePolicy.setHeightForWidth(self.find_in_transcript_btn.sizePolicy().hasHeightForWidth())
        self.find_in_transcript_btn.setSizePolicy(sizePolicy)
        self.find_in_transcript_btn.setMinimumSize(QSize(100, 30))
        self.find_in_transcript_btn.setFont(font)
        self.find_in_transcript_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.find_in_transcript_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"padding: 0 10px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-find-in-page.png", QSize(), QIcon.Normal, QIcon.On)
        self.find_in_transcript_btn.setIcon(icon1)

        self.gridLayout.addWidget(self.find_in_transcript_btn, 1, 1, 1, 1)


        self.retranslateUi(TranscribeEditor)

        QMetaObject.connectSlotsByName(TranscribeEditor)
    # setupUi

    def retranslateUi(self, TranscribeEditor):
        TranscribeEditor.setWindowTitle(QCoreApplication.translate("TranscribeEditor", u"Edit Transcript", None))
        self.edit_transcribed_text_edit.setPlaceholderText(QCoreApplication.translate("TranscribeEditor", u"Your automatically transcribed text will appear hear...", None))
        self.save_transcript_btn.setText(QCoreApplication.translate("TranscribeEditor", u"Save", None))
        self.close_transcript_dialog.setText(QCoreApplication.translate("TranscribeEditor", u"Close", None))
        self.find_in_transcript_btn.setText(QCoreApplication.translate("TranscribeEditor", u"Find...", None))
    # retranslateUi

