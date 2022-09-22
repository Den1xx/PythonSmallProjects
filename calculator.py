import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm,self).__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(200,200,500,500)
        self.initUI()

    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText('Sayi 1: ')
        self.lbl_sayi1.move(50,30)

        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)
    
        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText('Sayi 2: ')
        self.lbl_sayi2.move(50,80)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,32)

        self.btn_toplama = QtWidgets.QPushButton(self)
        self.btn_toplama.setText('toplama')
        self.btn_toplama.move(150,130)
        self.btn_toplama.clicked.connect(self.hesapla)

        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText('çıkarma')
        self.btn_cikar.move(150,170)
        self.btn_cikar.clicked.connect(self.hesapla)

        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText('çarpma')
        self.btn_carp.move(150,210)
        self.btn_carp.clicked.connect(self.hesapla)

        self.btn_bolme = QtWidgets.QPushButton(self)
        self.btn_bolme.setText('bölme')
        self.btn_bolme.move(150,250)
        self.btn_bolme.clicked.connect(self.hesapla)

        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText('sonuç')
        self.lbl_sonuc.move(150,290)


    def hesapla(self):
        sender = self.sender()
        result = 0
        if sender.text() == 'toplama':
            result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        elif sender.text() == 'çıkarma':
            result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        elif sender.text() == 'çarpma':
            result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        elif sender.text() == 'bölme':
            result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())

        self.lbl_sonuc.setText('Sonuç '+ str(result))

def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()   

        