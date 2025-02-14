import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedWidget
)
from PyQt6.QtCore import Qt

from DeepSeek.dungeon import Dungeon


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Menu")
        self.setGeometry(100, 100, 800, 600)

        # Central widget and stacked widget
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Create the main menu widget
        self.main_menu_widget = self.create_main_menu()
        self.central_widget.addWidget(self.main_menu_widget)

        # Create the Dungeon game widget
        self.dungeon_game = Dungeon()
        self.central_widget.addWidget(self.dungeon_game)

        # Connect the Dungeon's back_to_menu_signal to switch back to the main menu
        self.dungeon_game.back_to_menu_signal.connect(self.switch_to_main_menu)

    def create_main_menu(self):
        """Create the main menu widget."""
        widget = QWidget()
        layout = QVBoxLayout()
        buttons_layout = QVBoxLayout()

        # Game buttons
        self.dungeon_button = QPushButton("Dungeon")
        self.coliseum_button = QPushButton("Coliseum")
        self.ragnorak_button = QPushButton("Ragnorak")
        self.gallery_button = QPushButton("Gallery")

        # Add buttons to layout
        buttons_layout.addWidget(self.dungeon_button)
        buttons_layout.addWidget(self.coliseum_button)
        buttons_layout.addWidget(self.ragnorak_button)
        buttons_layout.addWidget(self.gallery_button)

        # Connect buttons to switch to the respective minigame
        self.dungeon_button.clicked.connect(lambda: self.switch_to_game(1))
        self.coliseum_button.clicked.connect(lambda: self.switch_to_game(2))
        self.ragnorak_button.clicked.connect(lambda: self.switch_to_game(3))
        self.gallery_button.clicked.connect(lambda: self.switch_to_game(4))

        # Bottom layout for settings and version
        bottom_layout = QHBoxLayout()

        layout.addLayout(buttons_layout)
        layout.addStretch()
        layout.addLayout(bottom_layout)

        # Settings button
        self.settings_button = QPushButton("Settings")
        bottom_layout.addWidget(self.settings_button, alignment=Qt.AlignmentFlag.AlignLeft)

        # Version label
        self.version_label = QLabel("Version 1.0")
        bottom_layout.addWidget(self.version_label, alignment=Qt.AlignmentFlag.AlignRight)

        widget.setLayout(layout)
        return widget

    def switch_to_game(self, index):
        """Switch to the minigame at the specified index."""
        self.central_widget.setCurrentIndex(index)

    def switch_to_main_menu(self):
        """Switch back to the main menu."""
        self.central_widget.setCurrentIndex(0)