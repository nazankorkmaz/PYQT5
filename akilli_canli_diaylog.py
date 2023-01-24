# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# Akıllı Diyalog Uyarı Ekranı Örneği
#YAZI RENGİ VE TİPİ DEĞİŞTİRİLİR VE YANLIŞ OLDUĞUNDA HATA MESAJI VE FOCUSLANMA GERÇEKLEŞİR

class yaziTipiDiyalog2 (QDialog):
    def __init__(self, parent = None):
        super (yaziTipiDiyalog2,self).__init__(parent)
        self.parent = parent
        self.setAttribute(Qt.WA_DeleteOnClose)
        
        izgara = QGridLayout()
        
        
        izgara.addWidget(QLabel("Yazı Tipi:"), 0,0,1,1) 
        self.yaziTipiListe = QFontComboBox()
        self.yaziTipiListe.setCurrentFont(QFont(self.parent.yaziTipi))
        izgara.addWidget(self.yaziTipiListe,0,1,1,1)   
        
        
        izgara.addWidget(QLabel("Yazı Rengi:"), 1,0,1,1)   
        self.renkKutu = QLineEdit(self.parent.yaziRengi)  #edit edilebilir boşluk
        izgara.addWidget(self.renkKutu,1,1,1,1)
        
        
        
        dugmeKutusu = QDialogButtonBox(QDialogButtonBox.Ok|
                                       QDialogButtonBox.Cancel)
        
        dugmeKutusu.button(QDialogButtonBox.Ok).setText("Tamam")
        dugmeKutusu.button(QDialogButtonBox.Cancel).setText("Vazgeç")
    
        
        dugmeKutusu.button(QDialogButtonBox.Ok).clicked.connect(self.kabul)
        dugmeKutusu.button(QDialogButtonBox.Cancel).clicked.connect(self.reject)
        
        izgara.addWidget(dugmeKutusu,2,0,1,2)  # 1,2 dedğim için sağa dayalı butonlar bu da QDialogButtondan kaynaklı
        
        self.setLayout(izgara)
        self.setWindowTitle("Yazı Tipi Ayarı")
        self.setWindowIcon (QIcon("roket.jpg"))
        
        
        
    def kabul (self):
        renk = self.renkKutu.text()  #QLİneEditten çektim 
        if not self.renkKontrol(renk):
            QMessageBox.warning(self, "Hatalı Renk", "Renk Kodu Yanlış. Düzeltiniz.") 
            self.renkKutu.selectAll() #yanlış renk girdiğimde uyarı ekranını kapattığımda gidicek ana ekranda renk yerine focuslanacak
            self.renkKutu.setFocus()
            return            
        self.parent.yaziTipi = self.yaziTipiListe.currentFont().family() #al ve koy
        self.parent.yaziRengi = renk
        self.parent.etiket.setText(self.parent.metin % (self.parent.yaziTipi, self.parent.yaziRengi))
        QDialog.accept(self)
        
        
    def renkKontrol (self, renk):
        if not len(renk)==7 : return False
        if not renk[0] =='#': return False
        for  i in renk[1:]:
            if not i.upper() in 'ABCDEF0123456789': 
                return False            
        return True
        
        

class AnaUygulamaAkilliDiyalog(QDialog):
    def __init__(self, parent = None):
        super (AnaUygulamaAkilliDiyalog,self).__init__(parent)
        self.yaziTipi = 'Verdana'
        self.yaziRengi = '#FF0000'
        self.metin = '<font size="+3" face="%s" color="%s"> görsel programlama dersi </font>'
        self.etiket = QLabel(self.metin % (self.yaziTipi, self.yaziRengi))
        
        kutu = QVBoxLayout()
        kutu.addWidget(self.etiket)
        
        yaziTipiDugme = QPushButton("Yazı Tipini ve Rengini Değiştir")
        yaziTipiDugme.clicked.connect(self.yaziTipiDegistir)
        kutu.addWidget(yaziTipiDugme)
        self.setLayout(kutu)
        
        self.setWindowTitle("Ana Uygulama")
        self.setWindowIcon (QIcon("roket.jpg"))
        
        
    def yaziTipiDegistir(self):
        diyalog = yaziTipiDiyalog2(self)
        diyalog.exec_()




uyg = QApplication([])
pencere = AnaUygulamaAkilliDiyalog()
pencere.show()
uyg.exec_() 


# Canlı diyalog bir çeşit akıllı diyalogtur. Kullanıcı açılan diyalogta
# değişiklikleri yapar ve değişiklikler anında yansıtılır. Aşağıdaki örnek
# canlı diyalog içindir. HTML etiketi yerine metin yazılabilir bir Qt parçacığı 
# kullanılmıştır.



"""

class yaziTipiDiyalog3 (QDialog):
    def __init__(self, parent = None):
        super (yaziTipiDiyalog3,self).__init__(parent)
        self.parent = parent
        
        #ızgara oluştur ve etiket ekle:
        izgara = QGridLayout()
        izgara.addWidget(QLabel('Yazı Tipi:'),0,0,1,1)
        
        # yazı tipi belirlemek için QFontComboBox oluştur ve ekle
        self.yaziTipiListe = QFontComboBox()
        
        
        
        simdikiYaziTipi = self.parent.metin.currentFont()       
        self.yaziTipiListe.setCurrentFont(simdikiYaziTipi)
        self.yaziTipiListe.activated.connect(self.yaziTipiDegistir)
        izgara.addWidget(self.yaziTipiListe,0,1,1,1)
        
        
        kapatDugmesi = QPushButton("Kapat")
        kapatDugmesi.clicked.connect(self.accept)
        izgara.addWidget(kapatDugmesi, 1,0,1,2)
        
        self.setLayout(izgara)
        self.setWindowTitle("Yazı Tipi Ayarı")
        self.setWindowIcon (QIcon("roket.jpg"))
        
    def yaziTipiDegistir(self):
        yaziTipi = self.yaziTipiListe.currentFont()
        self.parent.metin.setCurrentFont(yaziTipi)
        
    
    
class AnaUygulamaCanliDiyalog (QDialog):
    def __init__(self, parent = None):
        super (AnaUygulamaCanliDiyalog,self).__init__(parent)
        self.yaziTipiDiyalogNesnesi = None
    
        self.metin = QTextEdit()
        
        kutu = QVBoxLayout()
        kutu.addWidget(self.metin)
        
        yaziTipiDugme = QPushButton("Yazı Tipini Değiştir")
        yaziTipiDugme.clicked.connect(self.yaziTipiDegistir)
        kutu.addWidget(yaziTipiDugme)
        
        
        
        self.setLayout(kutu)
        self.setWindowTitle("Ana Uygulama")
        self.setWindowIcon (QIcon("roket.jpg"))
        
        
    def yaziTipiDegistir (self):
        if self.yaziTipiDiyalogNesnesi is None:
            self.yaziTipiDiyalogNesnesi = yaziTipiDiyalog3(self)
        
        self.yaziTipiDiyalogNesnesi.show()
        self.yaziTipiDiyalogNesnesi.raise_()
        self.yaziTipiDiyalogNesnesi.activateWindow()
        
        
       
    def closeEvent(self,olay):  # pencere kapanmadan önce diyalog nesnesi kapanır
        if self.yaziTipiDiyalogNesnesi:
            self.yaziTipiDiyalogNesnesi.close()
        
        


uyg = QApplication([])
pencere = AnaUygulamaCanliDiyalog()
pencere.show()
uyg.exec_() 

"""       