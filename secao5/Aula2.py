import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication(sys.argv)

botao = QPushButton('Texto do Botão')
botao.setStyleSheet('font-Size: 20px;')

botao1 = QPushButton('Botão 1')
botao1.setStyleSheet('font-Size: 20px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-Size: 20px;')

central_widget = QWidget()
layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao1, 1, 3, 1, 1)
layout.addWidget(botao2, 2, 2, 1, 2)

central_widget.show()  # central widget entre na hieraquia e mostre a janela
app.exec()
