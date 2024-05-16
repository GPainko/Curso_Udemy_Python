from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # configurando o layout básico
        self.cw = QWidget()  # centralWidget
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Título da Janela
        self.setWindowTitle('Calculadora')

    # última coisa a ser feita

    def adjustFixedSize(self):
       # Última coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
