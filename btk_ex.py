import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

#AD VE SOYADI PENCEREDE YAZAR ve terminalde

"""""""""""""""
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setWindowTitle("fist application")
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon('roket.jpg'))
        self.setToolTip('my tooltip')
        self.initUI()
    
    def initUI(self):
        self.lbl_name=QtWidgets.QLabel(self)
        self.lbl_name.setText('Adınız: ')
        self.lbl_name.move(50,30)

        self.lbl_surname=QtWidgets.QLabel(self)
        self.lbl_surname.setText('SoyAdınız: ')
        self.lbl_surname.move(50,70)

        self.lbl_result=QtWidgets.QLabel(self)
        self.lbl_result.resize(300,50)
        self.lbl_result.move(150,150)

        self.txt_name=QtWidgets.QLineEdit(self)
        self.txt_name.move(150,30)
        self.txt_name.resize(200,32)
        self.txt_surname=QtWidgets.QLineEdit(self)
        self.txt_surname.move(150,70)
        self.txt_surname.resize(200,32)

        self.btn_save=QtWidgets.QPushButton(self)
        self.btn_save.setText('Kaydet')
        self.btn_save.move(150,110)
        self.btn_save.clicked.connect(self.clicked)

    
    def clicked(self):
        print("butona tıklandı name:"+self.txt_name.text()+"  surname: "+self.txt_surname.text())
        self.lbl_result.setText('Sonuç: name '+self.txt_name.text()+"  surname: "+self.txt_surname.text())


def window():
    app=QApplication(sys.argv)
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
"""""""""
#AD VE SOYADI TERMİNALDE YAZAR


def window():
    app= QApplication(sys.argv)
    win=QMainWindow()

    win.setWindowTitle("fist application")
    win.setGeometry(200,200,500,500)
    win.setWindowIcon(QIcon('roket.jpg'))
    win.setToolTip('my tooltip')


    lbl_name=QtWidgets.QLabel(win)
    lbl_name.setText('Adınız: ')
    lbl_name.move(50,30)

    lbl_surname=QtWidgets.QLabel(win)
    lbl_surname.setText('SoyAdınız: ')
    lbl_surname.move(50,70)

    txt_name=QtWidgets.QLineEdit(win)
    txt_name.move(150,30)
    txt_surname=QtWidgets.QLineEdit(win)
    txt_surname.move(150,70)

    def clicked(self):
        print("butona tıklandı name:"+txt_name.text()+"  surname: "+txt_surname.text())

    btn_save=QtWidgets.QPushButton(win)
    btn_save.setText('Kaydet')
    btn_save.move(150,110)
    btn_save.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())

window()

