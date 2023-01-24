import sys
from PyQt5 import QtWidgets
"""""
#1
def Pencere():
    app= QtWidgets.QApplication(sys.argv)

    okay= QtWidgets.QPushButton("Tamam")
    cancel= QtWidgets.QPushButton("İptal")

    #QVBoxLayoutyapsaydık kutular alt alta yazılırdı gerisi hep aynıdır.Dikeybox yani
    h_box= QtWidgets.QHBoxLayout()  #yatay bir kutu artık

    h_box.addStretch()
    h_box.addWidget(okay)
    #h_box.addStretch()
    h_box.addWidget(cancel)

    #h_box.addStretch() #bunu eklediğin yere göre sola sağa hep yaslı kalıyorlar

#v nin için eh ı koyduk ve hep sağ altta kaldılar
    v_box = QtWidgets.QVBoxLayout()

    v_box.addStretch()
    v_box.addLayout(h_box)

   
    pencere= QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders")

    pencere.setLayout(v_box)
    pencere.setGeometry(100,100,500,500)

    pencere.show()
    sys.exit(app.exec_())

Pencere()
"""""

#2
"""
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.yazi_alani=QtWidgets.QLabel("Bana henüz tıklanmadı")
        self.buton= QtWidgets.QPushButton("Bana Tıkla")
        self.say=0

        v_box= QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        #alttakini yapmazsa sekmeyi açtıkça buton da uzar
        self.setLayout(h_box)

        self.buton.clicked.connect(self.click)

        self.show()
    def click(self):
        self.say += 1
        self.yazi_alani.setText("Bana " + str(self.say) + " defa tıklandı.")


app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())
"""

#3

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.yazi_alani=QtWidgets.QLineEdit()
        self.temizle=QtWidgets.QPushButton("Temizle")
        self.yazdir=QtWidgets.QPushButton("Yazdır")
        
        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.yazdir)
        v_box.addWidget(self.temizle)
        v_box.addStretch()
        
        self.setLayout(v_box)
        
        self.temizle.clicked.connect(self.click)
        self.yazdir.clicked.connect(self.click)
        
        self.show()
        
    def click(self):
        sender=self.sender()
        
        if sender.text()=="Temizle":
            self.yazi_alani.clear()
        else:
            print(self.yazi_alani.text())
    
app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())
