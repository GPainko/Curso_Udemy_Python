import sys

from main_window import MainWindow
from display import Display
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel
from variable import WINDOW_ICON_PATH


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    # Display
    display = Display()
    window.addToVLayout(display)

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Executa
    window.adjustFixedSize()

    window.show()
    app.exec()
