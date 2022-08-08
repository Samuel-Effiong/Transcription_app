
from PyQt5.QtCore import QRunnable


class Runner(QRunnable):
    def __init__(self, func, fname=None, selected_api=None, parent=None, *, ignore: dict = False):
        super(Runner, self).__init__()
        self.__func = func
        self.__parent = parent
        self.__fname = fname
        self.__selected_api = selected_api
        self.ignore = ignore

    def run(self) -> None:
        self.__func(self.__parent, fname=self.__fname, selected_api=self.__selected_api,
                    ignore=self.ignore)
