# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'display_info_widgethwSsiM.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.formLayout = QFormLayout(Form)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(12)
        self.formLayout.setVerticalSpacing(17)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.name_label = QLabel(Form)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setStyleSheet(u"font-weight: bold;")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name_label)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.size_label = QLabel(Form)
        self.size_label.setObjectName(u"size_label")
        self.size_label.setStyleSheet(u"font-weight: bold;\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.size_label)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.length_label = QLabel(Form)
        self.length_label.setObjectName(u"length_label")
        self.length_label.setStyleSheet(u"font-weight: bold;")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.length_label)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.no_of_channels_label = QLabel(Form)
        self.no_of_channels_label.setObjectName(u"no_of_channels_label")
        self.no_of_channels_label.setStyleSheet(u"font-weight: bold;\n"
"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.no_of_channels_label)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, 39, -1)
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font-weight: bold;")

        self.horizontalLayout.addWidget(self.label_10)

        self.transcription_status_label = QLabel(Form)
        self.transcription_status_label.setObjectName(u"transcription_status_label")
        self.transcription_status_label.setStyleSheet(u"font-weight: bold;\n"
"")

        self.horizontalLayout.addWidget(self.transcription_status_label)

        self.transcription_progressBar = QProgressBar(Form)
        self.transcription_progressBar.setObjectName(u"transcription_progressBar")
        self.transcription_progressBar.setValue(24)

        self.horizontalLayout.addWidget(self.transcription_progressBar)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Name:", None))
        self.name_label.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Size:", None))
        self.size_label.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Length:", None))
        self.length_label.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"No of Channels", None))
        self.no_of_channels_label.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"Transcription Status:", None))
        self.label_10.setText("")
        self.transcription_status_label.setText("")
    # retranslateUi

