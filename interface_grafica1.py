import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

def funcao1 ():
    label.setText('Botão 1')
    label.adjustSize()

def funcao2 ():
    label.setText('Botão 2')
    label.adjustSize()

def funcao3 ():
    valor_lido = le.text()
    label.setText(valor_lido)
    label.adjustSize()

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(800, 600)
janela.setWindowTitle('Primeira')

btn = QPushButton('Botão 1', janela)
btn.setGeometry(100, 100, 150, 80)
btn.setStyleSheet('background-color:blue; color:white')
btn.clicked.connect(funcao1)

btn2 = QPushButton('Botão 2', janela)
btn2.setGeometry(100, 300, 150, 80)
btn2.setStyleSheet('background-color:blue; color:white')
btn2.clicked.connect(funcao2)

btn3 = QPushButton('Botão 3', janela)
btn3.setGeometry(100, 500, 150, 80)
btn3.setStyleSheet('background-color:blue; color:white')
btn3.clicked.connect(funcao3)

label = QLabel('texto', janela)
label.move(400,100)
label.setStyleSheet('font-size:30px')


le = QLineEdit('', janela)
le.setGeometry(500, 500, 150, 40)


janela.show()


app.exec()