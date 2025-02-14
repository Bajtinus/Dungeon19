import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedWidget, QListWidget, QMessageBox
)
from PyQt6.QtCore import Qt


class Player:
    """Class to manage player attributes and logic."""
    def __init__(self, player_class):
        self.player_class = player_class
        self.level = 1
        self.experience = 0
        self.stars = 0
        self.coins = 100  # Starting coins for testing upgrades
        self.keys = 0
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.speed = 5

    def upgrade_attribute(self, attributes, cost):
        """
        Upgrade one or more attributes by specified amounts.

        Args:
            attributes (dict): A dictionary of attribute names and their respective increases.
                               Example: {"health": 10, "attack": 5}
            cost (int): The cost of the upgrade in coins.
        """
        if self.coins >= cost:
            for attr, increase in attributes.items():
                if hasattr(self, attr):
                    current_value = getattr(self, attr)
                    setattr(self, attr, current_value + increase)
                else:
                    raise ValueError(f"Invalid attribute: {attr}")
            self.coins -= cost
        else:
            raise ValueError("Not enough coins for the upgrade!")

    def get_attributes(self):
        """Return a dictionary of the player's attributes."""
        return {
            "level": self.level,
            "experience": self.experience,
            "stars": self.stars,
            "coins": self.coins,
            "keys": self.keys,
            "health": self.health,
            "attack": self.attack,
            "defense": self.defense,
            "speed": self.speed,
        }



class Header(QWidget):
    """Custom widget to display the player's attributes."""
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        # Labels for player attributes
        self.level_label = QLabel(f"Level: {self.player.level}")
        self.experience_label = QLabel(f"Experience: {self.player.experience}")
        self.stars_label = QLabel(f"Stars: {self.player.stars}")
        self.coins_label = QLabel(f"Coins: {self.player.coins}")
        self.keys_label = QLabel(f"Keys: {self.player.keys}")
        self.health_label = QLabel(f"Health: {self.player.health}")
        self.attack_label = QLabel(f"Attack: {self.player.attack}")
        self.defense_label = QLabel(f"Defense: {self.player.defense}")
        self.speed_label = QLabel(f"Speed: {self.player.speed}")

        # Add labels to layout
        layout.addWidget(self.level_label)
        layout.addWidget(self.experience_label)
        layout.addWidget(self.stars_label)
        layout.addWidget(self.coins_label)
        layout.addWidget(self.keys_label)
        layout.addWidget(self.health_label)
        layout.addWidget(self.attack_label)
        layout.addWidget(self.defense_label)
        layout.addWidget(self.speed_label)

        self.setLayout(layout)

    def update_attributes(self):
        """Update the displayed attributes."""
        self.level_label.setText(f"Level: {self.player.level}")
        self.experience_label.setText(f"Experience: {self.player.experience}")
        self.stars_label.setText(f"Stars: {self.player.stars}")
        self.coins_label.setText(f"Coins: {self.player.coins}")
        self.keys_label.setText(f"Keys: {self.player.keys}")
        self.health_label.setText(f"Health: {self.player.health}")
        self.attack_label.setText(f"Attack: {self.player.attack}")
        self.defense_label.setText(f"Defense: {self.player.defense}")
        self.speed_label.setText(f"Speed: {self.player.speed}")


class EnemyList(QWidget):
    """Placeholder widget for the list of enemies."""
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Enemy List (To be implemented)")
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)


class Upgrades(QWidget):
    """Widget containing buttons for upgrading the player."""
    def __init__(self, player, header):
        super().__init__()
        self.player = player
        self.header = header
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        # Upgrade buttons
        self.health_button = QPushButton("Upgrade Health (+10)")
        self.attack_button = QPushButton("Upgrade Attack (+5)")
        self.defense_button = QPushButton("Upgrade Defense (+5)")
        self.speed_button = QPushButton("Upgrade Speed (+5)")
        self.combo_upgrade_button = QPushButton("Combo Upgrade (Health +10, Attack +5)")

        # Connect buttons to upgrade methods
        self.health_button.clicked.connect(lambda: self.upgrade({"health": 10}, cost=5))
        self.attack_button.clicked.connect(lambda: self.upgrade({"attack": 5}, cost=5))
        self.defense_button.clicked.connect(lambda: self.upgrade({"defense": 5}, cost=5))
        self.speed_button.clicked.connect(lambda: self.upgrade({"speed": 5}, cost=5))
        self.combo_upgrade_button.clicked.connect(lambda: self.upgrade({"health": 10, "attack": 5}, cost=10))

        # Add buttons to layout
        layout.addWidget(self.health_button)
        layout.addWidget(self.attack_button)
        layout.addWidget(self.defense_button)
        layout.addWidget(self.speed_button)
        layout.addWidget(self.combo_upgrade_button)

        self.setLayout(layout)

    def upgrade(self, attributes, cost):
        """Upgrade the specified attributes."""
        try:
            self.player.upgrade_attribute(attributes, cost)
            self.header.update_attributes()  # Update the displayed attributes
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

    def upgrade_health(self):
        if self.player.coins >= 5:
            self.player.upgrade_health()
            self.header.update_attributes()
        else:
            QMessageBox.warning(self, "Error", "Not enough coins!")

    def upgrade_attack(self):
        if self.player.coins >= 5:
            self.player.upgrade_attack()
            self.header.update_attributes()
        else:
            QMessageBox.warning(self, "Error", "Not enough coins!")

    def upgrade_defense(self):
        if self.player.coins >= 5:
            self.player.upgrade_defense()
            self.header.update_attributes()
        else:
            QMessageBox.warning(self, "Error", "Not enough coins!")

    def upgrade_speed(self):
        if self.player.coins >= 5:
            self.player.upgrade_speed()
            self.header.update_attributes()
        else:
            QMessageBox.warning(self, "Error", "Not enough coins!")


from PyQt6.QtCore import pyqtSignal  # Add this import

class Dungeon(QWidget):
    """Main widget for the Dungeon game."""
    back_to_menu_signal = pyqtSignal()  # Signal to notify MainMenu to switch back

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Step 1: Let the user choose a class
        self.class_selection = QListWidget()
        self.class_selection.addItems(["Warrior", "Mage", "Rogue", "Archer"])
        self.class_selection.itemClicked.connect(self.start_game)
        self.class_selection_label = QLabel("Choose your class:")
        layout.addWidget(self.class_selection_label)
        layout.addWidget(self.class_selection)

        # Step 2: Game layout (hidden initially)
        self.game_layout = QVBoxLayout()
        self.game_widget = QWidget()
        self.game_widget.setLayout(self.game_layout)
        self.game_widget.hide()
        layout.addWidget(self.game_widget)

        # Add a "Back to Menu" button
        self.back_button = QPushButton("Back to Menu")
        self.back_button.clicked.connect(self.back_to_menu)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def start_game(self, item):
        """Start the game after the user selects a class."""
        self.player = Player(item.text())  # Create player with selected class
        self.class_selection.hide()  # Hide class selection
        self.class_selection_label.hide()  # Hide class selection

        # Initialize game layout
        self.header = Header(self.player)
        self.enemy_list = EnemyList()
        self.upgrades = Upgrades(self.player, self.header)

        self.game_layout.addWidget(self.header)
        self.game_layout.addWidget(self.enemy_list)
        self.game_layout.addWidget(self.upgrades)

        self.game_widget.show()  # Show the game layout

    def back_to_menu(self):
        """Emit a signal to notify MainMenu to switch back."""
        self.back_to_menu_signal.emit()