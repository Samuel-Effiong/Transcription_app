# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainceYBdg.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *
from .resources_rc import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 795)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color:"
                        " rgb(255, 121, 198);\n"
"}\n"
"QTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:ho"
                        "rizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin"
                        ";\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/ico"
                        "ns/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top rig"
                        "ht;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    wi"
                        "dth: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color:"
                        " rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(7)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setStyleSheet(u"")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_open_file = QPushButton(self.topMenu)
        self.btn_open_file.setObjectName(u"btn_open_file")
        sizePolicy.setHeightForWidth(self.btn_open_file.sizePolicy().hasHeightForWidth())
        self.btn_open_file.setSizePolicy(sizePolicy)
        self.btn_open_file.setMinimumSize(QSize(0, 45))
        self.btn_open_file.setFont(font)
        self.btn_open_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_file.setLayoutDirection(Qt.LeftToRight)
        self.btn_open_file.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-folder-open.png);")

        self.verticalLayout_8.addWidget(self.btn_open_file)

        self.btn_new_file = QPushButton(self.topMenu)
        self.btn_new_file.setObjectName(u"btn_new_file")
        sizePolicy.setHeightForWidth(self.btn_new_file.sizePolicy().hasHeightForWidth())
        self.btn_new_file.setSizePolicy(sizePolicy)
        self.btn_new_file.setMinimumSize(QSize(0, 45))
        self.btn_new_file.setFont(font)
        self.btn_new_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new_file.setLayoutDirection(Qt.LeftToRight)
        self.btn_new_file.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_new_file)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_search = QPushButton(self.topMenu)
        self.btn_search.setObjectName(u"btn_search")
        sizePolicy.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy)
        self.btn_search.setMinimumSize(QSize(0, 45))
        self.btn_search.setFont(font)
        self.btn_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_search.setLayoutDirection(Qt.LeftToRight)
        self.btn_search.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-magnifying-glass.png);")

        self.verticalLayout_8.addWidget(self.btn_search)

        self.btn_transcribe = QPushButton(self.topMenu)
        self.btn_transcribe.setObjectName(u"btn_transcribe")
        sizePolicy.setHeightForWidth(self.btn_transcribe.sizePolicy().hasHeightForWidth())
        self.btn_transcribe.setSizePolicy(sizePolicy)
        self.btn_transcribe.setMinimumSize(QSize(0, 45))
        self.btn_transcribe.setFont(font)
        self.btn_transcribe.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_transcribe.setLayoutDirection(Qt.LeftToRight)
        self.btn_transcribe.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-speech.png);")

        self.verticalLayout_8.addWidget(self.btn_transcribe)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_find = QPushButton(self.extraTopMenu)
        self.btn_find.setObjectName(u"btn_find")
        sizePolicy.setHeightForWidth(self.btn_find.sizePolicy().hasHeightForWidth())
        self.btn_find.setSizePolicy(sizePolicy)
        self.btn_find.setMinimumSize(QSize(0, 45))
        self.btn_find.setFont(font)
        self.btn_find.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_find.setLayoutDirection(Qt.LeftToRight)
        self.btn_find.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-find-in-page.png);")

        self.verticalLayout_11.addWidget(self.btn_find)

        self.btn_replace = QPushButton(self.extraTopMenu)
        self.btn_replace.setObjectName(u"btn_replace")
        sizePolicy.setHeightForWidth(self.btn_replace.sizePolicy().hasHeightForWidth())
        self.btn_replace.setSizePolicy(sizePolicy)
        self.btn_replace.setMinimumSize(QSize(0, 45))
        self.btn_replace.setFont(font)
        self.btn_replace.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_replace.setLayoutDirection(Qt.LeftToRight)
        self.btn_replace.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_replace)

        self.btn_font = QPushButton(self.extraTopMenu)
        self.btn_font.setObjectName(u"btn_font")
        sizePolicy.setHeightForWidth(self.btn_font.sizePolicy().hasHeightForWidth())
        self.btn_font.setSizePolicy(sizePolicy)
        self.btn_font.setMinimumSize(QSize(0, 45))
        self.btn_font.setFont(font)
        self.btn_font.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_font.setLayoutDirection(Qt.LeftToRight)
        self.btn_font.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_font)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setStyleSheet(u"")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.pagesContainer)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 10, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.home)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setContentsMargins(0, 0, -1, 0)
        self.additional_information_frame = QFrame(self.home)
        self.additional_information_frame.setObjectName(u"additional_information_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.additional_information_frame.sizePolicy().hasHeightForWidth())
        self.additional_information_frame.setSizePolicy(sizePolicy3)
        self.additional_information_frame.setMaximumSize(QSize(350, 16777215))
        self.additional_information_frame.setStyleSheet(u"background-color: #495472;")
        self.additional_information_frame.setFrameShape(QFrame.StyledPanel)
        self.additional_information_frame.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.additional_information_frame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(19)
        self.formLayout_2.setContentsMargins(7, 30, 16, -1)
        self.label_4 = QLabel(self.additional_information_frame)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setFamily(u"Cambria")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(9)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"font: 75 12pt \"Cambria\";\n"
"color: white;")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.teacher_name_line_edit = QLineEdit(self.additional_information_frame)
        self.teacher_name_line_edit.setObjectName(u"teacher_name_line_edit")
        self.teacher_name_line_edit.setMinimumSize(QSize(0, 30))
        self.teacher_name_line_edit.setFont(font)
        self.teacher_name_line_edit.setStyleSheet(u"border-radius: 8px;\n"
"color: white;")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.teacher_name_line_edit)

        self.label_5 = QLabel(self.additional_information_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"font: 75 12pt \"Cambria\";\n"
"color: white;")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.theme_name_line_edit = QLineEdit(self.additional_information_frame)
        self.theme_name_line_edit.setObjectName(u"theme_name_line_edit")
        self.theme_name_line_edit.setMinimumSize(QSize(0, 30))
        self.theme_name_line_edit.setFont(font)
        self.theme_name_line_edit.setStyleSheet(u"border-radius: 5px;\n"
"color: white;")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.theme_name_line_edit)

        self.label_6 = QLabel(self.additional_information_frame)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setFamily(u"Cambria")
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(9)
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"font: 75 11pt \"Cambria\";\n"
"color: white;")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.coordinator_name_line_edit = QLineEdit(self.additional_information_frame)
        self.coordinator_name_line_edit.setObjectName(u"coordinator_name_line_edit")
        self.coordinator_name_line_edit.setMinimumSize(QSize(0, 30))
        self.coordinator_name_line_edit.setFont(font)
        self.coordinator_name_line_edit.setStyleSheet(u"border-radius: 5px;\n"
"color: white;")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.coordinator_name_line_edit)


        self.gridLayout_3.addWidget(self.additional_information_frame, 0, 0, 4, 1)

        self.file_editing_main_layout = QGridLayout()
        self.file_editing_main_layout.setObjectName(u"file_editing_main_layout")
        self.show_additional_information_frame_push_button = QPushButton(self.home)
        self.show_additional_information_frame_push_button.setObjectName(u"show_additional_information_frame_push_button")
        self.show_additional_information_frame_push_button.setMinimumSize(QSize(0, 22))
        self.show_additional_information_frame_push_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_additional_information_frame_push_button.setStyleSheet(u"border: none;\n"
"background-color: #BD92F4;\n"
"padding: 0 5px;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-arrow-circle-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.show_additional_information_frame_push_button.setIcon(icon4)

        self.file_editing_main_layout.addWidget(self.show_additional_information_frame_push_button, 3, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.file_editing_main_layout.addItem(self.horizontalSpacer_8, 3, 1, 1, 1)

        self.text_editor = QTextEdit(self.home)
        self.text_editor.setObjectName(u"text_editor")
        self.text_editor.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.file_editing_main_layout.addWidget(self.text_editor, 2, 0, 1, 2)

        self.warning_display = QLabel(self.home)
        self.warning_display.setObjectName(u"warning_display")
        sizePolicy3.setHeightForWidth(self.warning_display.sizePolicy().hasHeightForWidth())
        self.warning_display.setSizePolicy(sizePolicy3)
        self.warning_display.setFont(font)
        self.warning_display.setStyleSheet(u"background-color: rgb(170, 0, 0);\n"
"border-radius: 10px;\n"
"padding: 3px 0;\n"
"color: white;")
        self.warning_display.setAlignment(Qt.AlignCenter)

        self.file_editing_main_layout.addWidget(self.warning_display, 1, 0, 1, 2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(23)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 15, -1, -1)
        self.heading_line_edit = QLineEdit(self.home)
        self.heading_line_edit.setObjectName(u"heading_line_edit")
        sizePolicy.setHeightForWidth(self.heading_line_edit.sizePolicy().hasHeightForWidth())
        self.heading_line_edit.setSizePolicy(sizePolicy)
        self.heading_line_edit.setMinimumSize(QSize(0, 40))
        self.heading_line_edit.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font: 17pt \"Poor Richard\";\n"
"color: white;")

        self.horizontalLayout_14.addWidget(self.heading_line_edit)

        self.categories_combobox = QComboBox(self.home)
        self.categories_combobox.addItem("")
        self.categories_combobox.addItem("")
        self.categories_combobox.addItem("")
        self.categories_combobox.setObjectName(u"categories_combobox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.categories_combobox.sizePolicy().hasHeightForWidth())
        self.categories_combobox.setSizePolicy(sizePolicy4)
        self.categories_combobox.setFont(font)
        self.categories_combobox.setAutoFillBackground(False)
        self.categories_combobox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.categories_combobox.setIconSize(QSize(16, 16))
        self.categories_combobox.setFrame(True)

        self.horizontalLayout_14.addWidget(self.categories_combobox)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(4)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.text_unique_identifier = QLabel(self.home)
        self.text_unique_identifier.setObjectName(u"text_unique_identifier")
        sizePolicy1.setHeightForWidth(self.text_unique_identifier.sizePolicy().hasHeightForWidth())
        self.text_unique_identifier.setSizePolicy(sizePolicy1)
        self.text_unique_identifier.setStyleSheet(u"font: 14pt \"Rockwell\";")

        self.horizontalLayout_18.addWidget(self.text_unique_identifier)

        self.text_unique_identifier_line_edit = QLineEdit(self.home)
        self.text_unique_identifier_line_edit.setObjectName(u"text_unique_identifier_line_edit")
        self.text_unique_identifier_line_edit.setMinimumSize(QSize(70, 34))
        self.text_unique_identifier_line_edit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"Rockwell\";\n"
"padding-right: 5px")
        self.text_unique_identifier_line_edit.setMaxLength(3)
        self.text_unique_identifier_line_edit.setFrame(True)
        self.text_unique_identifier_line_edit.setClearButtonEnabled(False)

        self.horizontalLayout_18.addWidget(self.text_unique_identifier_line_edit)

        self.date_edit = QPushButton(self.home)
        self.date_edit.setObjectName(u"date_edit")
        sizePolicy4.setHeightForWidth(self.date_edit.sizePolicy().hasHeightForWidth())
        self.date_edit.setSizePolicy(sizePolicy4)
        self.date_edit.setMinimumSize(QSize(100, 30))
        self.date_edit.setFont(font)
        self.date_edit.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_edit.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-pen-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.date_edit.setIcon(icon5)

        self.horizontalLayout_18.addWidget(self.date_edit)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_14.setStretch(0, 3)
        self.horizontalLayout_14.setStretch(2, 1)

        self.file_editing_main_layout.addLayout(self.horizontalLayout_14, 0, 0, 1, 2)


        self.gridLayout_3.addLayout(self.file_editing_main_layout, 2, 2, 1, 2)

        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon7)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font6);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy5)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.gridLayout_4 = QGridLayout(self.search)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(13)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(15)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.search_line_edit = QLineEdit(self.search)
        self.search_line_edit.setObjectName(u"search_line_edit")
        self.search_line_edit.setMinimumSize(QSize(12, 40))
        self.search_line_edit.setStyleSheet(u"background-color: C8C8C8;\n"
"border-radius: 18px;")

        self.verticalLayout_20.addWidget(self.search_line_edit)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_20.addLayout(self.horizontalLayout_7)


        self.gridLayout_4.addLayout(self.verticalLayout_20, 2, 1, 2, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(38, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(19)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.keyword_checkbox = QCheckBox(self.search)
        self.keyword_checkbox.setObjectName(u"keyword_checkbox")
        self.keyword_checkbox.setChecked(True)

        self.horizontalLayout_17.addWidget(self.keyword_checkbox)

        self.semantic_checkbox = QCheckBox(self.search)
        self.semantic_checkbox.setObjectName(u"semantic_checkbox")

        self.horizontalLayout_17.addWidget(self.semantic_checkbox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_4)


        self.gridLayout_4.addLayout(self.horizontalLayout_17, 1, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 2)
        self.gridLayout_4.setColumnStretch(2, 1)
        self.stackedWidget.addWidget(self.search)
        self.search_result = QWidget()
        self.search_result.setObjectName(u"search_result")
        self.gridLayout_8 = QGridLayout(self.search_result)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.search_result_display_gridlayout = QGridLayout()
        self.search_result_display_gridlayout.setObjectName(u"search_result_display_gridlayout")
        self.advanced_search_filter_pushbutton = QPushButton(self.search_result)
        self.advanced_search_filter_pushbutton.setObjectName(u"advanced_search_filter_pushbutton")
        self.advanced_search_filter_pushbutton.setStyleSheet(u"border-radius: 8px;\n"
"padding: 5px 5px;\n"
"background-color: rgb(33, 37, 43);")
        self.advanced_search_filter_pushbutton.setIcon(icon4)

        self.search_result_display_gridlayout.addWidget(self.advanced_search_filter_pushbutton, 1, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.search_result_display_gridlayout.addItem(self.horizontalSpacer_11, 1, 0, 1, 1)

        self.search_result_display = QTableView(self.search_result)
        self.search_result_display.setObjectName(u"search_result_display")
        self.search_result_display.setStyleSheet(u"border: none;")
        self.search_result_display.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.search_result_display.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.search_result_display.setAutoScroll(True)
        self.search_result_display.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.search_result_display.setSelectionMode(QAbstractItemView.SingleSelection)
        self.search_result_display.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.search_result_display.setSortingEnabled(True)
        self.search_result_display.horizontalHeader().setMinimumSectionSize(150)
        self.search_result_display.horizontalHeader().setStretchLastSection(True)
        self.search_result_display.verticalHeader().setProperty("showSortIndicator", True)
        self.search_result_display.verticalHeader().setStretchLastSection(False)

        self.search_result_display_gridlayout.addWidget(self.search_result_display, 0, 0, 1, 2)


        self.gridLayout_8.addLayout(self.search_result_display_gridlayout, 2, 2, 1, 1)

        self.additional_filter_frame = QFrame(self.search_result)
        self.additional_filter_frame.setObjectName(u"additional_filter_frame")
        sizePolicy3.setHeightForWidth(self.additional_filter_frame.sizePolicy().hasHeightForWidth())
        self.additional_filter_frame.setSizePolicy(sizePolicy3)
        self.additional_filter_frame.setStyleSheet(u"background-color: #495472;\n"
"color: white;")
        self.additional_filter_frame.setFrameShape(QFrame.StyledPanel)
        self.additional_filter_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.additional_filter_frame)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalSpacer_3 = QSpacerItem(20, 240, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_3, 3, 1, 1, 1)

        self.label_2 = QLabel(self.additional_filter_frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_10.addWidget(self.label_2, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.additional_filter_frame)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: white;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.year_category = QComboBox(self.groupBox)
        self.year_category.addItem("")
        self.year_category.addItem("")
        self.year_category.addItem("")
        self.year_category.addItem("")
        self.year_category.addItem("")
        self.year_category.addItem("")
        self.year_category.addItem("")
        self.year_category.addItem("")
        self.year_category.addItem("")
        self.year_category.addItem("")
        self.year_category.addItem("")
        self.year_category.setObjectName(u"year_category")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.year_category)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: white;\n"
"")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.month_category = QComboBox(self.groupBox)
        self.month_category.addItem("")
        self.month_category.addItem("")
        self.month_category.addItem("")
        self.month_category.addItem("")
        self.month_category.addItem("")
        self.month_category.addItem("")
        self.month_category.addItem("")
        self.month_category.addItem("")
        self.month_category.addItem("")
        self.month_category.addItem("")
        self.month_category.addItem("")
        self.month_category.addItem("")
        self.month_category.addItem("")
        self.month_category.setObjectName(u"month_category")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.month_category)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.days_category = QComboBox(self.groupBox)
        self.days_category.addItem("")
        self.days_category.addItem("")
        self.days_category.addItem("")
        self.days_category.addItem("")
        self.days_category.addItem("")
        self.days_category.addItem("")
        self.days_category.addItem("")
        self.days_category.addItem("")
        self.days_category.setObjectName(u"days_category")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.days_category)


        self.gridLayout_10.addWidget(self.groupBox, 1, 0, 1, 2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_9 = QLabel(self.additional_filter_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: white;")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.teacher_combobox = QComboBox(self.additional_filter_frame)
        self.teacher_combobox.addItem("")
        self.teacher_combobox.setObjectName(u"teacher_combobox")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.teacher_combobox)

        self.label_10 = QLabel(self.additional_filter_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: white;")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.coordinator_combobox = QComboBox(self.additional_filter_frame)
        self.coordinator_combobox.addItem("")
        self.coordinator_combobox.setObjectName(u"coordinator_combobox")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.coordinator_combobox)


        self.gridLayout_10.addLayout(self.formLayout_3, 2, 0, 1, 2)


        self.gridLayout_8.addWidget(self.additional_filter_frame, 2, 3, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.back_to_search_home = QPushButton(self.search_result)
        self.back_to_search_home.setObjectName(u"back_to_search_home")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.back_to_search_home.sizePolicy().hasHeightForWidth())
        self.back_to_search_home.setSizePolicy(sizePolicy6)
        self.back_to_search_home.setMinimumSize(QSize(0, 26))
        self.back_to_search_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_to_search_home.setStyleSheet(u"border-radius: 8px;\n"
"padding: 5px 5px;\n"
"background-color: rgb(33, 37, 43);")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-arrow-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_to_search_home.setIcon(icon8)

        self.horizontalLayout_6.addWidget(self.back_to_search_home)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.search_line_edit_small = QLineEdit(self.search_result)
        self.search_line_edit_small.setObjectName(u"search_line_edit_small")
        self.search_line_edit_small.setMinimumSize(QSize(0, 25))
        self.search_line_edit_small.setStyleSheet(u"border-radius: 10px;\n"
"color: white;\n"
"background-color: rgb(33, 37, 43);\n"
"")
        self.search_line_edit_small.setClearButtonEnabled(True)

        self.horizontalLayout_6.addWidget(self.search_line_edit_small)

        self.search_push_button_small = QPushButton(self.search_result)
        self.search_push_button_small.setObjectName(u"search_push_button_small")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.search_push_button_small.sizePolicy().hasHeightForWidth())
        self.search_push_button_small.setSizePolicy(sizePolicy7)
        self.search_push_button_small.setMinimumSize(QSize(53, 0))
        self.search_push_button_small.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_push_button_small.setStyleSheet(u"padding: 2px 0px;\n"
"border-radius: 10px;\n"
"background-color: rgb(33, 37, 43);")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_push_button_small.setIcon(icon9)
        self.search_push_button_small.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.search_push_button_small)


        self.gridLayout_8.addLayout(self.horizontalLayout_6, 1, 2, 1, 2)

        self.stackedWidget.addWidget(self.search_result)
        self.transcribe = QWidget()
        self.transcribe.setObjectName(u"transcribe")
        self.gridLayout_5 = QGridLayout(self.transcribe)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(9, -1, 9, -1)
        self.transcribe_file_list = QListWidget(self.transcribe)
        self.transcribe_file_list.setObjectName(u"transcribe_file_list")
        sizePolicy5.setHeightForWidth(self.transcribe_file_list.sizePolicy().hasHeightForWidth())
        self.transcribe_file_list.setSizePolicy(sizePolicy5)
        self.transcribe_file_list.setAlternatingRowColors(True)
        self.transcribe_file_list.setBatchSize(7)

        self.gridLayout_5.addWidget(self.transcribe_file_list, 2, 1, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_7)


        self.gridLayout_5.addLayout(self.horizontalLayout_15, 1, 0, 1, 4)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(22)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 9)
        self.select_audio_button = QPushButton(self.transcribe)
        self.select_audio_button.setObjectName(u"select_audio_button")
        sizePolicy3.setHeightForWidth(self.select_audio_button.sizePolicy().hasHeightForWidth())
        self.select_audio_button.setSizePolicy(sizePolicy3)
        self.select_audio_button.setMinimumSize(QSize(100, 30))
        self.select_audio_button.setFont(font)
        self.select_audio_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.select_audio_button.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"padding: 0 10px;")

        self.horizontalLayout_10.addWidget(self.select_audio_button)

        self.label = QLabel(self.transcribe)
        self.label.setObjectName(u"label")

        self.horizontalLayout_10.addWidget(self.label)

        self.voice_recognition_api_combobox = QComboBox(self.transcribe)
        self.voice_recognition_api_combobox.addItem("")
        self.voice_recognition_api_combobox.addItem("")
        self.voice_recognition_api_combobox.setObjectName(u"voice_recognition_api_combobox")
        sizePolicy.setHeightForWidth(self.voice_recognition_api_combobox.sizePolicy().hasHeightForWidth())
        self.voice_recognition_api_combobox.setSizePolicy(sizePolicy)
        self.voice_recognition_api_combobox.setFont(font)
        self.voice_recognition_api_combobox.setAutoFillBackground(False)
        self.voice_recognition_api_combobox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.voice_recognition_api_combobox.setIconSize(QSize(16, 16))
        self.voice_recognition_api_combobox.setFrame(True)

        self.horizontalLayout_10.addWidget(self.voice_recognition_api_combobox)

        self.horizontalSpacer_3 = QSpacerItem(70, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.transcribe_date_label = QLabel(self.transcribe)
        self.transcribe_date_label.setObjectName(u"transcribe_date_label")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.transcribe_date_label.sizePolicy().hasHeightForWidth())
        self.transcribe_date_label.setSizePolicy(sizePolicy8)
        self.transcribe_date_label.setStyleSheet(u"font: 14pt \"Rockwell\";")

        self.horizontalLayout_13.addWidget(self.transcribe_date_label)

        self.transcribe_date_edit = QPushButton(self.transcribe)
        self.transcribe_date_edit.setObjectName(u"transcribe_date_edit")
        sizePolicy4.setHeightForWidth(self.transcribe_date_edit.sizePolicy().hasHeightForWidth())
        self.transcribe_date_edit.setSizePolicy(sizePolicy4)
        self.transcribe_date_edit.setMinimumSize(QSize(100, 30))
        self.transcribe_date_edit.setFont(font)
        self.transcribe_date_edit.setCursor(QCursor(Qt.PointingHandCursor))
        self.transcribe_date_edit.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.transcribe_date_edit.setIcon(icon5)

        self.horizontalLayout_13.addWidget(self.transcribe_date_edit)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_13)


        self.gridLayout_5.addLayout(self.horizontalLayout_10, 0, 0, 1, 4)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.transcribe_progress_display_4 = QLabel(self.transcribe)
        self.transcribe_progress_display_4.setObjectName(u"transcribe_progress_display_4")
        sizePolicy3.setHeightForWidth(self.transcribe_progress_display_4.sizePolicy().hasHeightForWidth())
        self.transcribe_progress_display_4.setSizePolicy(sizePolicy3)
        self.transcribe_progress_display_4.setMinimumSize(QSize(400, 0))
        self.transcribe_progress_display_4.setMaximumSize(QSize(400, 16777215))
        self.transcribe_progress_display_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.transcribe_progress_display_4.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.transcribe_progress_display_4)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 0, 39, -1)
        self.transcription_status_label_2 = QLabel(self.transcribe)
        self.transcription_status_label_2.setObjectName(u"transcription_status_label_2")
        sizePolicy4.setHeightForWidth(self.transcription_status_label_2.sizePolicy().hasHeightForWidth())
        self.transcription_status_label_2.setSizePolicy(sizePolicy4)
        self.transcription_status_label_2.setStyleSheet(u"font-weight: bold;\n"
"")
        self.transcription_status_label_2.setWordWrap(True)

        self.horizontalLayout_21.addWidget(self.transcription_status_label_2)


        self.verticalLayout_24.addLayout(self.horizontalLayout_21)

        self.transcription_progressBar_2 = QProgressBar(self.transcribe)
        self.transcription_progressBar_2.setObjectName(u"transcription_progressBar_2")
        sizePolicy4.setHeightForWidth(self.transcription_progressBar_2.sizePolicy().hasHeightForWidth())
        self.transcription_progressBar_2.setSizePolicy(sizePolicy4)
        self.transcription_progressBar_2.setValue(24)

        self.verticalLayout_24.addWidget(self.transcription_progressBar_2)

        self.internet_connection_layout = QHBoxLayout()
        self.internet_connection_layout.setObjectName(u"internet_connection_layout")
        self.continue_transcription = QPushButton(self.transcribe)
        self.continue_transcription.setObjectName(u"continue_transcription")
        sizePolicy7.setHeightForWidth(self.continue_transcription.sizePolicy().hasHeightForWidth())
        self.continue_transcription.setSizePolicy(sizePolicy7)
        self.continue_transcription.setMinimumSize(QSize(62, 30))
        self.continue_transcription.setFont(font)
        self.continue_transcription.setCursor(QCursor(Qt.PointingHandCursor))
        self.continue_transcription.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"border-radius: 10px;\n"
"width: 20px;")
        self.continue_transcription.setIcon(icon3)

        self.internet_connection_layout.addWidget(self.continue_transcription)

        self.internet_connectivity_display = QLabel(self.transcribe)
        self.internet_connectivity_display.setObjectName(u"internet_connectivity_display")
        self.internet_connectivity_display.setStyleSheet(u"font: italic 10pt \"Cambria\";")
        self.internet_connectivity_display.setWordWrap(True)

        self.internet_connection_layout.addWidget(self.internet_connectivity_display)


        self.verticalLayout_24.addLayout(self.internet_connection_layout)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_5)


        self.gridLayout_5.addLayout(self.verticalLayout_24, 2, 2, 1, 1)

        self.stackedWidget.addWidget(self.transcribe)

        self.gridLayout_6.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 32))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(32)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 3)
        self.loading_files_widget = QWidget(self.bottomBar)
        self.loading_files_widget.setObjectName(u"loading_files_widget")
        self.horizontalLayout_16 = QHBoxLayout(self.loading_files_widget)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 7, -1, 5)
        self.loading_files_label = QLabel(self.loading_files_widget)
        self.loading_files_label.setObjectName(u"loading_files_label")
        sizePolicy3.setHeightForWidth(self.loading_files_label.sizePolicy().hasHeightForWidth())
        self.loading_files_label.setSizePolicy(sizePolicy3)
        self.loading_files_label.setStyleSheet(u"color: white;")

        self.horizontalLayout_16.addWidget(self.loading_files_label)

        self.loading_files_progressbar = QProgressBar(self.loading_files_widget)
        self.loading_files_progressbar.setObjectName(u"loading_files_progressbar")
        sizePolicy7.setHeightForWidth(self.loading_files_progressbar.sizePolicy().hasHeightForWidth())
        self.loading_files_progressbar.setSizePolicy(sizePolicy7)
        self.loading_files_progressbar.setMinimumSize(QSize(200, 0))
        self.loading_files_progressbar.setStyleSheet(u"QProgressBar {\n"
"	border-style: none;\n"
"	text-align: center;\n"
"	border-radius: 10px;\n"
"	color: black;\n"
"}\n"
"\n"
"QProgressBar:chunk{\n"
"	background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"}")
        self.loading_files_progressbar.setValue(24)

        self.horizontalLayout_16.addWidget(self.loading_files_progressbar)

        self.loading_files_info_display = QLabel(self.loading_files_widget)
        self.loading_files_info_display.setObjectName(u"loading_files_info_display")
        sizePolicy1.setHeightForWidth(self.loading_files_info_display.sizePolicy().hasHeightForWidth())
        self.loading_files_info_display.setSizePolicy(sizePolicy1)
        self.loading_files_info_display.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_16.addWidget(self.loading_files_info_display)


        self.horizontalLayout_5.addWidget(self.loading_files_widget)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        sizePolicy3.setHeightForWidth(self.version.sizePolicy().hasHeightForWidth())
        self.version.setSizePolicy(sizePolicy3)
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.voice_recognition_api_combobox)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_open_file.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
        self.btn_new_file.setText(QCoreApplication.translate("MainWindow", u"New...", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btn_transcribe.setText(QCoreApplication.translate("MainWindow", u"Transcribe", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_find.setText(QCoreApplication.translate("MainWindow", u"Find...", None))
        self.btn_replace.setText(QCoreApplication.translate("MainWindow", u"Replace...", None))
        self.btn_font.setText(QCoreApplication.translate("MainWindow", u"Font...", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">God's Lighthouse </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#ffffff;\">eyes that see...ears that hears</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">The path to GOD is filled with divers trap"
                        "s, temptations and perils. But the wisdom of GOD will show you the way and keep you on it, but only love will ensure that you, on your own will, continue on the path and that you will remain faithful to the very end.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: GLH Media</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">It is not by believing in your mind, but in your heart that results in Righteousness</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">God Loves you</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"PyDracula APP - Theme with colors based on Dracula for Python.", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Teacher:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Theme:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Coordinator:", None))
        self.show_additional_information_frame_push_button.setText(QCoreApplication.translate("MainWindow", u"Add additional information", None))
        self.text_editor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Start typing here", None))
        self.warning_display.setText(QCoreApplication.translate("MainWindow", u"Warning: This file already exist", None))
        self.heading_line_edit.setText("")
        self.heading_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Heading", None))
        self.categories_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Sermons", None))
        self.categories_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Catalogs", None))
        self.categories_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Testimonies", None))

        self.text_unique_identifier.setText(QCoreApplication.translate("MainWindow", u"GLH-Sat 30 Apr, 2022-", None))
        self.date_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.search_line_edit.setText("")
        self.search_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Search Phrase e.g GOD powers are a demonstration of His love", None))
        self.keyword_checkbox.setText(QCoreApplication.translate("MainWindow", u"Keyword Search", None))
        self.semantic_checkbox.setText(QCoreApplication.translate("MainWindow", u"Semantic Search", None))
        self.advanced_search_filter_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Advanced Search Filters", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Advanced Search:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Year:", None))
        self.year_category.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.year_category.setItemText(1, QCoreApplication.translate("MainWindow", u"2016", None))
        self.year_category.setItemText(2, QCoreApplication.translate("MainWindow", u"2017", None))
        self.year_category.setItemText(3, QCoreApplication.translate("MainWindow", u"2018", None))
        self.year_category.setItemText(4, QCoreApplication.translate("MainWindow", u"2019", None))
        self.year_category.setItemText(5, QCoreApplication.translate("MainWindow", u"2020", None))
        self.year_category.setItemText(6, QCoreApplication.translate("MainWindow", u"2021", None))
        self.year_category.setItemText(7, QCoreApplication.translate("MainWindow", u"2022", None))
        self.year_category.setItemText(8, QCoreApplication.translate("MainWindow", u"2023", None))
        self.year_category.setItemText(9, QCoreApplication.translate("MainWindow", u"2024", None))
        self.year_category.setItemText(10, QCoreApplication.translate("MainWindow", u"2025", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Month:", None))
        self.month_category.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.month_category.setItemText(1, QCoreApplication.translate("MainWindow", u"January", None))
        self.month_category.setItemText(2, QCoreApplication.translate("MainWindow", u"Febraury", None))
        self.month_category.setItemText(3, QCoreApplication.translate("MainWindow", u"March", None))
        self.month_category.setItemText(4, QCoreApplication.translate("MainWindow", u"April", None))
        self.month_category.setItemText(5, QCoreApplication.translate("MainWindow", u"May", None))
        self.month_category.setItemText(6, QCoreApplication.translate("MainWindow", u"June", None))
        self.month_category.setItemText(7, QCoreApplication.translate("MainWindow", u"July", None))
        self.month_category.setItemText(8, QCoreApplication.translate("MainWindow", u"August", None))
        self.month_category.setItemText(9, QCoreApplication.translate("MainWindow", u"September", None))
        self.month_category.setItemText(10, QCoreApplication.translate("MainWindow", u"October", None))
        self.month_category.setItemText(11, QCoreApplication.translate("MainWindow", u"November", None))
        self.month_category.setItemText(12, QCoreApplication.translate("MainWindow", u"December", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Days:", None))
        self.days_category.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.days_category.setItemText(1, QCoreApplication.translate("MainWindow", u"Monday", None))
        self.days_category.setItemText(2, QCoreApplication.translate("MainWindow", u"Tuesday", None))
        self.days_category.setItemText(3, QCoreApplication.translate("MainWindow", u"Wednessday", None))
        self.days_category.setItemText(4, QCoreApplication.translate("MainWindow", u"Thursday", None))
        self.days_category.setItemText(5, QCoreApplication.translate("MainWindow", u"Friday", None))
        self.days_category.setItemText(6, QCoreApplication.translate("MainWindow", u"Saturday", None))
        self.days_category.setItemText(7, QCoreApplication.translate("MainWindow", u"Sunday", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Teacher:", None))
        self.teacher_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Coordinator:", None))
        self.coordinator_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

        self.back_to_search_home.setText(QCoreApplication.translate("MainWindow", u"Back to Search", None))
        self.search_line_edit_small.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter search phrase", None))
        self.search_push_button_small.setText("")
        self.select_audio_button.setText(QCoreApplication.translate("MainWindow", u"Select Media files", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Choose Recognition Engine:", None))
        self.voice_recognition_api_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Google Speech Recognition", None))
        self.voice_recognition_api_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Houndify Voice Recognition", None))

        self.transcribe_date_label.setText(QCoreApplication.translate("MainWindow", u"Sat 30 Apr, 2022", None))
        self.transcribe_date_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.transcribe_progress_display_4.setText("")
        self.transcription_status_label_2.setText("")
        self.continue_transcription.setText("")
        self.internet_connectivity_display.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p >Pause transcription</p><p><span style=\" color:#ff0728;\">This is an experimental feature...may cause crashes</span></p></body></html>", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.loading_files_label.setText(QCoreApplication.translate("MainWindow", u"Loading files:", None))
        self.loading_files_info_display.setText("")
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

