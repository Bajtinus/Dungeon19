import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout,
                             QComboBox, QProgressBar)

import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QListWidget

class Player:
    def __init__(self):
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.speed = 8
        self.experience = 50  # Example values
        self.keys = 2
        self.coins = 150
        self.stars = 3

    def upgrade_attack(self):
        self.attack += 5

    def upgrade_defense(self):
        self.defense += 3

class HeaderWidget(QWidget):
    def __init__(self, player):
        super().__init__()
        layout = QVBoxLayout()

        top_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        self.player_image = QLabel()
        self.player_image.setPixmap(QPixmap("player.png").scaled(64, 64, Qt.AspectRatioMode.KeepAspectRatio))
        self.player_image.setFixedSize(64, 64)

        self.exp_bar = QProgressBar()
        self.exp_bar.setValue(player.experience)
        self.keys_label = QLabel(f"Keys: {player.keys}")
        self.coins_label = QLabel(f"Coins: {player.coins}")
        self.stars_label = QLabel(f"Stars: {player.stars}")

        self.health_label = QLabel(f"Health: {player.health}")
        self.attack_label = QLabel(f"Attack: {player.attack}")
        self.defense_label = QLabel(f"Defense: {player.defense}")
        self.speed_label = QLabel(f"Speed: {player.speed}")

        top_layout.addWidget(self.player_image)
        top_layout.addWidget(self.exp_bar)
        top_layout.addWidget(self.keys_label)
        top_layout.addWidget(self.coins_label)
        top_layout.addWidget(self.stars_label)

        bottom_layout.addWidget(self.health_label)
        bottom_layout.addWidget(self.attack_label)
        bottom_layout.addWidget(self.defense_label)
        bottom_layout.addWidget(self.speed_label)

        layout.addLayout(top_layout)
        layout.addLayout(bottom_layout)
        self.setLayout(layout)



class Dungeon(QWidget):
    def __init__(self, app, stack):
        super().__init__()
        self.app = app
        self.stack = stack
        self.init_dungeon()

    def init_dungeon(self):
        self.player = Player()

        layout = QVBoxLayout()
        self.header = HeaderWidget(self.player)
        self.enemy_list = QListWidget()
        self.enemy_list.addItem("Goblin")
        self.enemy_list.addItem("Skeleton")
        self.enemy_list.addItem("Orc")

        self.upgrade_attack_button = QPushButton("Upgrade Attack")
        self.upgrade_defense_button = QPushButton("Upgrade Defense")
        self.back_button = QPushButton("Back to Menu")

        self.upgrade_attack_button.clicked.connect(self.upgrade_attack)
        self.upgrade_defense_button.clicked.connect(self.upgrade_defense)
        self.back_button.clicked.connect(self.go_back)

        layout.addWidget(self.header)
        layout.addWidget(self.enemy_list)
        layout.addWidget(self.upgrade_attack_button)
        layout.addWidget(self.upgrade_defense_button)
        layout.addWidget(self.back_button)
        self.setLayout(layout)

    def upgrade_attack(self):
        self.player.upgrade_attack()
        self.header.update_stats(self.player)

    def upgrade_defense(self):
        self.player.upgrade_defense()
        self.header.update_stats(self.player)

    def go_back(self):
        self.stack.setCurrentWidget(self.stack.widget(0))

    def reset_dungeon(self):
        self.init_dungeon()