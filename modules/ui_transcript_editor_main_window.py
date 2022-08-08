# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transcript_editor_main_windowQjfOyl.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_TranscribeEditorMain(object):
    def setupUi(self, TranscribeEditorMain):
        if TranscribeEditorMain.objectName():
            TranscribeEditorMain.setObjectName(u"TranscribeEditorMain")
        TranscribeEditorMain.resize(486, 447)
        self.centralwidget = QWidget(TranscribeEditorMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.save_transcript_btn = QPushButton(self.centralwidget)
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

        self.gridLayout.addWidget(self.save_transcript_btn, 0, 0, 1, 1)

        self.find_in_transcript_btn = QPushButton(self.centralwidget)
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

        self.gridLayout.addWidget(self.find_in_transcript_btn, 0, 1, 1, 1)

        self.edit_transcribed_text_edit = QTextEdit(self.centralwidget)
        self.edit_transcribed_text_edit.setObjectName(u"edit_transcribed_text_edit")
        self.edit_transcribed_text_edit.setEnabled(True)
        self.edit_transcribed_text_edit.setMinimumSize(QSize(200, 200))
        self.edit_transcribed_text_edit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.edit_transcribed_text_edit, 1, 0, 1, 3)

        self.close_transcript_dialog = QPushButton(self.centralwidget)
        self.close_transcript_dialog.setObjectName(u"close_transcript_dialog")
        sizePolicy.setHeightForWidth(self.close_transcript_dialog.sizePolicy().hasHeightForWidth())
        self.close_transcript_dialog.setSizePolicy(sizePolicy)
        self.close_transcript_dialog.setMinimumSize(QSize(100, 30))
        self.close_transcript_dialog.setFont(font)
        self.close_transcript_dialog.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_transcript_dialog.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"padding: 0 10px;")

        self.gridLayout.addWidget(self.close_transcript_dialog, 2, 2, 1, 1)

        TranscribeEditorMain.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(TranscribeEditorMain)
        self.statusbar.setObjectName(u"statusbar")
        TranscribeEditorMain.setStatusBar(self.statusbar)

        self.retranslateUi(TranscribeEditorMain)

        QMetaObject.connectSlotsByName(TranscribeEditorMain)
    # setupUi

    def retranslateUi(self, TranscribeEditorMain):
        TranscribeEditorMain.setWindowTitle(QCoreApplication.translate("TranscribeEditorMain", u"MainWindow", None))
        self.save_transcript_btn.setText(QCoreApplication.translate("TranscribeEditorMain", u"Save", None))
        self.find_in_transcript_btn.setText(QCoreApplication.translate("TranscribeEditorMain", u"Find...", None))
        self.edit_transcribed_text_edit.setPlaceholderText(QCoreApplication.translate("TranscribeEditorMain", u"Your automatically transcribed text will appear hear...", None))
        self.close_transcript_dialog.setText(QCoreApplication.translate("TranscribeEditorMain", u"Close", None))
    # retranslateUi

