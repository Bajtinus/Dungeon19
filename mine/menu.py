from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QStackedLayout, QVBoxLayout, QPushButton, QHBoxLayout, QLabel

from mine.dungeon.dungeon import Dungeon


class Menu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.stack = QStackedLayout()

        self.menu = QWidget(self)
        self.dungeon = Dungeon(self)
        self.coliseum = QWidget(self) # TODO Coliseum(self)
        self.ragnorak = QWidget(self)# TODO Ragnorak(self)
        self.gallery = QWidget(self)# TODO Gallery(self)

        self.init_ui()

    def init_ui(self):
        self.setLayout(self.stack)

        self.dungeon.finished.connect(lambda: self.switch_to(0))

        menu_layout = QVBoxLayout()
        self.menu.setLayout(menu_layout)

        dungeon = QPushButton("Dungeon", self)
        dungeon.clicked.connect(lambda: self.switch_to(1))

        coliseum = QPushButton("Coliseum", self)
        coliseum.clicked.connect(lambda: self.switch_to(2))

        ragnorak = QPushButton("Ragnorak", self)
        ragnorak.clicked.connect(lambda: self.switch_to(3))

        gallery = QPushButton("Gallery", self)
        gallery.clicked.connect(lambda: self.switch_to(4))

        buttons_layout = QVBoxLayout()
        buttons_layout.setContentsMargins(100, 0, 100, 0)
        buttons_layout.addStretch()
        buttons_layout.addWidget(dungeon)
        buttons_layout.addWidget(coliseum)
        buttons_layout.addWidget(ragnorak)
        buttons_layout.addWidget(gallery)
        buttons_layout.addStretch()

        footer_layout = QHBoxLayout()

        footer_layout.addWidget(QPushButton("Settings", self))
        title = QLabel("Dungeon 19", self)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer_layout.addWidget(title, 1)
        footer_layout.addWidget(QLabel("0.0.1", self))

        buttons = QWidget()
        buttons.setLayout(buttons_layout)

        footer = QWidget()
        footer.setLayout(footer_layout)

        menu_layout.addWidget(buttons, 1)
        menu_layout.addWidget(footer)

        self.stack.addWidget(self.menu)
        self.stack.addWidget(self.dungeon)
        self.stack.addWidget(self.coliseum)
        self.stack.addWidget(self.ragnorak)
        self.stack.addWidget(self.gallery)

    def switch_to(self, index):
        self.stack.setCurrentIndex(index)

