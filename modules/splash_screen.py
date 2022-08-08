
from qt_core import *
from . app_settings import Themes
from . ui_simple_splashscreen import Ui_SplashScreen


class SplashScreen(QMainWindow):
    def __init__(self, *, main_window):
        super(SplashScreen, self).__init__()
        self.main_window = main_window
        self.themes = Themes()
        self.settings = self.themes.settings
        self.themes = self.themes.items

        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)

        # REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(10)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # QTIME ==> START
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)

        # TIMER IN MILLISECONDS
        self.timer.start(35)

        self.counter = 0
        self.setup_splash()

        self.show()

    def setup_splash(self):
        style_sheet = f"""
        background-color: {self.themes['app_color']['white']};
        border-radius: 10px;
        """
        self.ui.dropShadowFrame.setStyleSheet(style_sheet)

        app_name = self.settings['app_name'].split()
        app_name = f"<strong>{app_name[0]}</strong> {' '.join(app_name[1:])}"
        self.ui.label_title.setText(app_name)

        description = f"<i>{self.settings['app_name_description']}</i>"
        self.ui.label_description.setText(description)
        self.ui.label_credit.setText(f"<i>{self.settings['copyright']}</i>")

    def progress(self):
        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(self.counter)

        # CLOSE SPLASH SCREEN AND OPEN APP
        if self.counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW THE WINDOW
            main = self.main_window()
            main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        self.counter += 1

