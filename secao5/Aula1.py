# QApplication e QpushButton de PySide6.Qtwidgets
# QApplication -> O widget principal da aplicação
# QpushButton -> um botão
# Qtwidgets -> onde estão os widgets do PySide6

import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton('Texto do Botão')
botao.setStyleSheet('font-Size: 20px;')
botao.show()  # Adicionar o widget na hieraquia e exibe a janela

botao2 = QPushButton('Botão 2')
botao2.show()

app.exec()  # executa o loop da execução
