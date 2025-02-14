from PyQt6.QtWidgets import QApplication, QMainWindow

from mine.menu import Menu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dungeon 19")
        self.setGeometry(100, 100, 512, 756)
        self.setCentralWidget(Menu(self))


class Game(QApplication):
    def __init__(self):
        super().__init__([])
        with open("mine/styles.qss", "r") as f:
            self.setStyleSheet(f.read())
        self.window = MainWindow()
        self.window.show()

if __name__ == '__main__':
    game = Game()
    game.exec()

