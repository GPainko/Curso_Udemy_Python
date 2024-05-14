import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication, QPushButton, QMainWindow, QWidget, QGridLayout)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha Janela')

botao = QPushButton('Texto do Botão')
botao.setStyleSheet('font-Size: 20px;')

# botao1 = QPushButton('Botão 1')
# botao1.setStyleSheet('font-Size: 20px;')

# botao2 = QPushButton('Botão 2')
# botao2.setStyleSheet('font-Size: 20px;')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
# layout.addWidget(botao1, 1, 3, 1, 1)
# layout.addWidget(botao2, 2, 2, 1, 2)


@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('O meu slot foi executado')
    return inner


@Slot()
def outro_slot_example(checked):
    print('Está Marcado ?', checked)


@Slot()
def terceiro_slot(action):
    def inner():
        outro_slot_example(action.isChecked())
    return inner


# StatusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# Menu
menu = window.menuBar()
priemiro_menu = menu.addMenu('Qualquer coisa')
primeira_acao = priemiro_menu.addAction('Primeira Ação')
primeira_acao.triggered.connect(slot_example(status_bar))

segunda_acao = priemiro_menu.addAction('SegundaAção')
segunda_acao.setCheckable(True)
segunda_acao.toggled.connect(outro_slot_example)
segunda_acao.hovered.connect(terceiro_slot(segunda_acao))

botao.clicked.connect(terceiro_slot(segunda_acao))

window.show()
app.exec()
