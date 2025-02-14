from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QSpacerItem, \
    QSizePolicy


class MainMenu(QMainWindow):
    def __init__(self, app, stack):
        super().__init__()
        self.app = app
        self.stack = stack
        self.setWindowTitle("Main Menu")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        button_layout = QVBoxLayout()
        bottom_layout = QHBoxLayout()

        self.dungeon_button = QPushButton("Dungeon")
        self.coliseum_button = QPushButton("Coliseum")
        self.ragnarok_button = QPushButton("Ragnarok")
        self.gallery_button = QPushButton("Gallery")

        button_layout.addWidget(self.dungeon_button)
        button_layout.addWidget(self.coliseum_button)
        button_layout.addWidget(self.ragnarok_button)
        button_layout.addWidget(self.gallery_button)

        self.settings_button = QPushButton("Settings")
        self.version_label = QLabel("0.0.1")

        bottom_layout.addWidget(self.settings_button)
        bottom_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        bottom_layout.addWidget(self.version_label)

        main_layout.addStretch()
        main_layout.addLayout(button_layout)
        main_layout.addStretch()
        main_layout.addLayout(bottom_layout)

        central_widget.setLayout(main_layout)

        self.dungeon_button.clicked.connect(self.open_dungeon)

    def open_dungeon(self):
        dungeon = self.stack.widget(1)
        dungeon.reset_dungeon()
        self.stack.setCurrentWidget(1)
