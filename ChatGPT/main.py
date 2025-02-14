import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget, QWidget, QVBoxLayout, QPushButton

from ChatGPT.dungeon import Dungeon
from ChatGPT.menu import MainMenu


class MiniGame(QWidget):
    def __init__(self, app, stack):
        super().__init__()
        self.app = app
        self.stack = stack

        layout = QVBoxLayout()
        self.back_button = QPushButton("Back to Menu")
        self.back_button.clicked.connect(self.go_back)
        layout.addWidget(self.back_button)
        self.setLayout(layout)

    def go_back(self):
        self.stack.setCurrentWidget(self.stack.widget(0))


class GameApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        self.stack = QStackedWidget()
        self.menu = MainMenu(self, self.stack)

        self.stack.addWidget(self.menu)

        self.stack.addWidget(Dungeon(self, self.stack))

        self.stack.setCurrentWidget(self.menu)
        self.stack.show()

def main():
    app = GameApp(sys.argv)
    app.exec()
    sys.exit()

if __name__ == "__main__":
    main()
