from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QWidget

from mine.player import Novice


class Dungeon(QWidget):
    finished = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.player = Novice()
        self.init_ui()

    def keyPressEvent(self, a0):
        if a0.key() == Qt.Key.Key_Escape:
            self.finished.emit()

    def init_ui(self):
        pass

    def reset(self):
        pass