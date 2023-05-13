from PyQt6 import uic, QtWidgets

def exibir_mensagem():
    dado_lido = janela.lineEdit.text()
    print(dado_lido)
    janela.lineEdit.setText('')



app = QtWidgets.QApplication([])
janela = uic.loadUi('caixa de mensagem.ui')
janela.pushButton.clicked.connect(exibir_mensagem)

janela.show()
app.exec()

