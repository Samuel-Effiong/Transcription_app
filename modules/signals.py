from PyQt5.QtCore import QObject, pyqtSignal


# progress_indicator = NewType('Progress_Indicator', Any)
# fname = NewType("Fname", str)


class Signals(QObject):
    transcription_completion_signal = pyqtSignal(str)
    progress_signal = pyqtSignal()
