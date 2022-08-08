# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simple_splashscreenOPSAJx.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        SplashScreen.setStyleSheet(u"background-color: black;")
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(51, 56, 83);\n"
"	color: rgb(200, 200, 200);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 90, 661, 61))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(255, 135, 237);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(-20, 150, 661, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(94, 101, 163);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 270, 541, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(100, 115, 163);	\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	text-align: center;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QProgressBar:chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.472, x2:1, y2:0.483, stop:0 rgba(255, 133, 245, 255), stop:0.982955 rgba(170, 85, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(-30, 300, 661, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"color: rgb(94, 101, 163);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credit = QLabel(self.dropShadowFrame)
        self.label_credit.setObjectName(u"label_credit")
        self.label_credit.setGeometry(QRect(0, 350, 641, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(11)
        self.label_credit.setFont(font3)
        self.label_credit.setStyleSheet(u"color: rgb(94, 101, 163);")
        self.label_credit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<strong>YOUR</strong> APP NAME", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:600;\">APP</span> DESCRIPTION</p><p><br/></p></body></html>", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p>Loading...</p></body></html>", None))
        self.label_credit.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><strong>Created:</strong> Nkopuruk Samuel E.</p></body></html>", None))
    # retranslateUi

