from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QProgressBar, QScrollArea
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
import sys
import random

class Player:
    def __init__(self):
        self.hp = 250
        self.attack = 25
        self.defense = 10
        self.speed = 40
        self.keys = 3
        self.coins = 200
        self.stars = 30
        self.exp = 50

class HeaderWidget(QWidget):
    def __init__(self, player):
        super().__init__()
        self.player = player
        layout = QVBoxLayout()

        # Top row
        top_layout = QHBoxLayout()
        self.avatar = QLabel()
        self.avatar.setPixmap(QPixmap("icons/player.png").scaled(50, 50))
        self.exp_bar = QProgressBar()
        self.exp_bar.setValue(self.player.exp)

        self.keys_label = QLabel(f"🔑 {self.player.keys}")
        self.coins_label = QLabel(f"🟤 {self.player.coins}")
        self.stars_label = QLabel(f"⭐ {self.player.stars}")

        top_layout.addWidget(self.avatar)
        top_layout.addWidget(self.exp_bar)
        top_layout.addWidget(self.keys_label)
        top_layout.addWidget(self.coins_label)
        top_layout.addWidget(self.stars_label)

        # Bottom row
        bottom_layout = QHBoxLayout()
        self.hp_label = QLabel(f"💛 {self.player.hp}")
        self.attack_label = QLabel(f"🟥 {self.player.attack}")
        self.defense_label = QLabel(f"🔷 {self.player.defense}")
        self.speed_label = QLabel(f"🟩 {self.player.speed}")

        bottom_layout.addWidget(self.hp_label)
        bottom_layout.addWidget(self.attack_label)
        bottom_layout.addWidget(self.defense_label)
        bottom_layout.addWidget(self.speed_label)

        layout.addLayout(top_layout)
        layout.addLayout(bottom_layout)
        self.setLayout(layout)

class Enemy(QWidget):
    def __init__(self, level, damage, hp, attack, defense, speed, rewards):
        super().__init__()
        layout = QHBoxLayout()

        # Enemy Icon & Level
        self.icon_label = QLabel()
        self.icon_label.setPixmap(QPixmap("icons/skull.png").scaled(40, 40))
        self.level_label = QLabel(f"{level}")

        icon_layout = QVBoxLayout()
        icon_layout.addWidget(self.icon_label)
        icon_layout.addWidget(self.level_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Enemy Stats
        self.damage_label = QLabel(f"💜 {damage}")
        self.hp_label = QLabel(f"💛 {hp}")
        self.attack_label = QLabel(f"🟥 {attack}")
        self.defense_label = QLabel(f"🔷 {defense}")
        self.speed_label = QLabel(f"🟩 {speed}")

        stats_layout = QHBoxLayout()
        stats_layout.addWidget(self.damage_label)
        stats_layout.addWidget(self.hp_label)
        stats_layout.addWidget(self.attack_label)
        stats_layout.addWidget(self.defense_label)
        stats_layout.addWidget(self.speed_label)

        # Rewards Section
        self.rewards_label = QLabel(" ".join(rewards))

        layout.addLayout(icon_layout)
        layout.addLayout(stats_layout)
        layout.addWidget(self.rewards_label)

        self.setLayout(layout)

class MenuScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dungeon 18")
        self.setGeometry(100, 100, 400, 600)
        self.setStyleSheet(open("styles.qss", "r").read())

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Buttons
        self.dungeon_btn = QPushButton("Dungeon")
        self.colosseum_btn = QPushButton("Colosseum")
        self.ragnarok_btn = QPushButton("Ragnarok")
        self.gallery_btn = QPushButton("Gallery")

        for btn in [self.dungeon_btn, self.colosseum_btn, self.ragnarok_btn, self.gallery_btn]:
            btn.setIcon(QIcon("icons/dungeon.png"))  # Replace with appropriate icons
            layout.addWidget(btn)

        # Version label
        self.version_label = QLabel("1.6.2")
        self.version_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.version_label)

        # Connect buttons
        self.dungeon_btn.clicked.connect(self.open_dungeon)

    def open_dungeon(self):
        self.dungeon_screen = DungeonScreen()
        self.dungeon_screen.show()
        self.hide()

class DungeonScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dungeon")
        self.setGeometry(100, 100, 400, 600)
        self.setStyleSheet(open("styles.qss", "r").read())

        self.player = Player()

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Header (Player Info)
        self.header = HeaderWidget(self.player)
        layout.addWidget(self.header)

        # Enemy List (Scrollable)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.enemy_container = QWidget()
        self.enemy_layout = QVBoxLayout()

        # Generate random enemies
        for _ in range(10):
            rewards = ["💛 40", "🟥 25", "🔷 10", "🟩 40", ""]
            enemy = Enemy(random.randint(1, 10),
                          random.randint(10, 50),
                          random.randint(50, 200),
                          random.randint(10, 50),
                          random.randint(5, 30),
                          random.randint(10, 50),
                          random.choice(rewards))
            self.enemy_layout.addWidget(enemy)

        self.enemy_container.setLayout(self.enemy_layout)
        self.scroll_area.setWidget(self.enemy_container)
        layout.addWidget(self.scroll_area)

        # Footer (Upgrade Buttons)
        self.upgrade_hp = QPushButton("HP")
        self.upgrade_attack = QPushButton("Attack")
        self.upgrade_defense = QPushButton("Defense")
        self.upgrade_speed = QPushButton("Speed")

        footer_layout = QHBoxLayout()
        for btn in [self.upgrade_hp, self.upgrade_attack, self.upgrade_defense, self.upgrade_speed]:
            footer_layout.addWidget(btn)

        layout.addLayout(footer_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuScreen()
    window.show()
    sys.exit(app.exec())