from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout, QApplication
from PyQt6.QtGui import QPixmap


class IconWidget(QWidget):
    def __init__(self, icon_name, parent=None):
        """
        Simple icon widget
        :param icon_name: path starting from assets/icons/...
        :param parent: parent widget
        """
        super().__init__(parent)
        path = f"assets/icons/{icon_name}"

        self.icon_label = QLabel(self)
        self.icon_label.setPixmap(QPixmap(path))

        layout = QVBoxLayout()
        layout.addWidget(self.icon_label)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])
    icon = IconWidget("gui/sword")
    icon.show()
    app.exec()
