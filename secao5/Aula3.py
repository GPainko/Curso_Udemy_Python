import sys
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


def slot_example(status_bar):
    status_bar.showMessage('O meu slot foi executado')


# StatusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# Menu
menu = window.menuBar()
priemiro_menu = menu.addMenu('Qualquer coisa')
primeira_acao = priemiro_menu.addAction('Primeira Ação')
primeira_acao.triggered.connect(lambda: slot_example(status_bar))

window.show()
app.exec()
