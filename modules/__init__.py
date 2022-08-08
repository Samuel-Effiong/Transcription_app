# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# GUI FILE
from . ui_main import Ui_MainWindow

# APP SETTINGS
from . app_settings import Settings, Settings_Json, Themes

# IMPORT FUNCTIONS
from . ui_functions import *

# APP FUNCTIONS
from . app_functions import *

# CUSTOM WIDGETS
from . custom_ui_functions import *

# DATABASE
from . database_operations import DataBase

# SPEECH ENGINE
from . transcriber_engine import TranscribeEngine

# SPLASH SCREEN
from . splash_screen import SplashScreen

# Transcribe Editor
from . ui_transcript_editor import Ui_TranscribeEditor
from . ui_transcript_editor_main_window import Ui_TranscribeEditorMain

# Search Result display row interface
from . display_search_row import SearchResultDisplayRow


# SIGNALS
from . signals import Signals