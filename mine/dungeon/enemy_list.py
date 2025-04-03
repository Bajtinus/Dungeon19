from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QProgressBar, QGridLayout, QLabel

from mine.decorations import IconWidget
from mine.player import Novice, Player


class Enemy:
    pass



class EnemyWidget(QWidget):
    def __init__(self, enemy_type: str, level: int, reward: (str, int), parent=None):
        super().__init__(parent)

class EnemyList(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.full_list = []
