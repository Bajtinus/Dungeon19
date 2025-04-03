from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QProgressBar, QGridLayout, QLabel

from mine.decorations import IconWidget
from mine.dungeon.enemy_list import EnemyList
from mine.player import Novice, Player


class HeaderWidget(QWidget):
    def __init__(self, player, parent):
        super().__init__(parent)
        self.player: Player = player

        self.icons: dict[str:IconWidget] = {
            "avatar": IconWidget("avatars/novice.png", self),
            "key": IconWidget("gui/key.svg", self),
            "coin": IconWidget("gui/coin.svg", self),
            "star": IconWidget("gui/star.svg", self),
            "health": IconWidget("gui/health.svg", self),
            "sword": IconWidget("gui/sword.svg", self),
            "shield": IconWidget("gui/shield.svg", self),
            "boot": IconWidget("gui/boot.svg", self)
        }
        self.xp_bar = QProgressBar(self)
        self.keys = QLabel(self)
        self.coins = QLabel(self)
        self.stars = QLabel(self)
        self.health = QLabel(self)
        self.attack = QLabel(self)
        self.defense = QLabel(self)
        self.speed = QLabel(self)

        self.init_ui()
        self.update_stats()

    def init_ui(self):
        layout = QGridLayout()

        layout.addWidget(self.icons["avatar"], 0, 0, 2, 2)
        layout.addWidget(self.xp_bar, 0, 2, 1, 2)
        layout.addWidget(self.icons["key"], 0, 4)
        layout.addWidget(self.keys, 0, 5)
        layout.addWidget(self.icons["coin"], 0, 6)
        layout.addWidget(self.coins, 0, 7)
        layout.addWidget(self.icons["star"], 0, 8)
        layout.addWidget(self.stars, 0, 9)
        layout.addWidget(self.icons["health"], 1, 2)
        layout.addWidget(self.health, 1, 3)
        layout.addWidget(self.icons["sword"], 1, 4)
        layout.addWidget(self.attack, 1, 5)
        layout.addWidget(self.icons["shield"], 1, 6)
        layout.addWidget(self.defense, 1, 7)
        layout.addWidget(self.icons["boot"], 1, 8)
        layout.addWidget(self.speed, 1, 9)

        self.setLayout(layout)

    def update_stats(self):

        self.xp_bar.setValue(self.player.experience)
        self.xp_bar.setMaximum(self.player.max_xp)

        self.keys.setText(str(self.player.keys))
        self.coins.setText(str(self.player.coins))
        self.stars.setText(str(self.player.stars))
        self.health.setText(str(self.player.health))
        self.attack.setText(str(self.player.attack))
        self.defense.setText(str(self.player.defense))
        self.speed.setText(str(self.player.speed))


class Upgrades(QWidget):
    def __init__(self):
        super().__init__()


class Dungeon(QWidget):
    finished = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.player = Novice()

        self.header = HeaderWidget(self.player, self)
        self.enemies = EnemyList()
        self.upgrades = Upgrades()

        self.init_ui()

    def keyPressEvent(self, a0):
        if a0.key() == Qt.Key.Key_Escape:
            self.finished.emit()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(self.header)
        layout.addWidget(self.enemies, 1)
        layout.addWidget(self.upgrades)

    def reset(self):
        pass
