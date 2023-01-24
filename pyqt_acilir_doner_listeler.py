# -*- coding: utf-8 -*-


# Diyaloglar
# Kullanıcı ile etkileşim Diyaloglar ile gerçekleşir.
# Bir diyalog ana pencere üstünde açılan, üzerinde Qt parçacıkları bulunan
# bir uyarı veya programa veri girişi yapılan pencerelerdir.
# Akılsız, Akıllı ve Canlı Diyaloglar vardır.

# 1.Akılsız Diyaloglar: parçacıkların değerleri çağıran fonksiyon 
# tarafından ayarlanır. Ve kullanıcının yaptığı değişiklikler yine çağıran fonksiyon
#tarafından alınır.

"""


#YAZI TİPİ AKILSIZ DİYALOG MANTIĞI İLE DEĞİŞTİRİLİR.

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class yaziTipiDiyalog (QDialog):
    def __init__(self, parent=None):
        super(yaziTipiDiyalog,self).__init__(parent)
        izgara = QGridLayout()
        # widgetlar tek tek eklenir.
        izgara.addWidget(QLabel ('Yazı Tipi:'),0,0,1,1)
        self.yaziTipiListe= QComboBox()
        self.yaziTipiListe.addItems(('Arial','Times New Roman', 'Verdana', 'Comic Sans MS'))
        self.yaziTipiListe.setCurrentIndex(2) #başlangıçta verdana seçtik
        izgara.addWidget(self.yaziTipiListe,0,1,1,1)
        
        kabulDugme = QPushButton("Tamam")
        iptalDugme = QPushButton("İptal")
        kabulDugme.setDefault(True) # kabulDugme ön tanımlı yapıldı. Şart değil.
        
        dugmeKutusu = QHBoxLayout()
        dugmeKutusu.addWidget(kabulDugme)
        dugmeKutusu.addWidget(iptalDugme)
        izgara.addLayout(dugmeKutusu, 1,0,1,2)
        
        kabulDugme.clicked.connect(self.accept) #bastığımda kabul et demek
        iptalDugme.clicked.connect(self.reject)
        
        self.setLayout(izgara)
        self.resize(300, 100)
        
        self.setWindowTitle("YazıTipi Ayarı")
        self.setWindowIcon(QIcon("roket.jpg"))
        
        
        
class AnaUygulamaAkılsızDiyalog (QDialog):
    def __init__(self, parent=None):
        super(AnaUygulamaAkılsızDiyalog,self).__init__(parent)
        self.yaziTipi = 'Verdana'
        self.metin = '<font color ="black" face="%s" size ="+3"> görsel programlama</font>'
        self.etiket = QLabel(self.metin % self.yaziTipi)
        kutu = QVBoxLayout()
        kutu.addWidget(self.etiket)
        
        yaziTipiDugme = QPushButton("Yazı Tipini Değiştir")
        yaziTipiDugme.clicked.connect(self.yaziTipiDegistir)
        kutu.addWidget(yaziTipiDugme)
        self.setLayout(kutu)
        self.setWindowTitle("Ana Uygulama")
        self.setWindowIcon(QIcon("roket.jpg"))
    
    def yaziTipiDegistir(self):
        diyalog = yaziTipiDiyalog()
        if diyalog.exec_():
            self.yaziTipi= diyalog.yaziTipiListe.currentText() #defaultta ne seçiliyse
            self.etiket.setText(self.metin % self.yaziTipi)
            
            
        
uyg = QApplication([]) 
pencere = AnaUygulamaAkılsızDiyalog() 
pencere.show()
uyg.exec_()        
        


yukarıdaki uygulamada "yazı tipini değiştir" butonuna basınca if içerisindeki
'diyalog.exec_()' sayesinde diyaloğun görünmesi sağlanmaktadır.
Kullanıcı, çağırdığı diyalogta 'Tamam' düğmesine basınca accept() döndürülür. Dolayısıyla
kullanıcı yaptığı ayarların uygulanmasına onay veriyor demektir. 'İptal' düğmesine basılır ise
reject () döndürülür. Bu da red anlamı taşır.
Diğer deyişle, diyalog.exec_() karşılaştırmasında accept, yani 1 gelirse, sonraki satırlar işletilecek demektir.
Red halinde ise, yani 0, kod daha fazla devam etmez. Diyalog ekranı kapanır.
"""""""""

#Akılsız diyaloglarda tüm işler kendisini çağıran fonksiyon tarafından yapılır.
#Akılsız diyaloglar yalnızca parçacıkları (widgets) ekranda görüntüler. Başka bir iş yapmaz.
#Bu nokta bazı durumlarda pratik kullanım sunarken birtakım dezavantajlar da getirir. En önemli dezavantajlarından bir tanesi
#diyalog penceresi açıldığında kullanıcı yaptığı değişiklikleri onay vermeden göremez. Onaylanan vaziyet ise geri alınamaz, 
#kalıcı olur. Bunun anlamı akılsız diyalog penceresi kendisini çağıran pencere ile etkileşmez.
#Akılsız diyaloglardaki bir diğer önemli dezavantaj bellek kullanım meselesidir. Akılsız diyalog pencereleri
#ister sağ üstteki kapatma simgesi ister onay düğmesi üzerinden kapansın pencere yalnızca görünmez olur.
#Bellekte yer tutmaya devam eder.
#Akıllı diyaloglar tüm bu dezavantajları ortadan kaldırır. Akıllı diyaloglarda çağıran penceredeki değişiklikler
#diyalog penceresinin kendi içerisinde yapılır. Diyalog kapatıldığında tüm işlemler yapıldığından doğrudan silinerek 
#bellekte yer tutmaz. Bu durum, diyaloğun başına 'self.setAttribute(Qt.WA_DeleteOnClose)' satırı eklenerek sağlanır.
#Bu satır akılsız diyaloglara eklenemez. Çünkü diyalog penceresi kapatıldıktan sonra çağıran fonksiyon diyalogtan
#veri alır.

#2
#AKILLI DİYALOG MANTIĞIYLA YAZI TİPİ DEĞİŞTİRİLİR

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class yaziTipiDiyalog2 (QDialog):
    def __init__(self, parent=None):
        super(yaziTipiDiyalog2,self).__init__(parent)
        self.parent = parent   #bir üstteki parentının etkilerinden etkilenir ve ona bağımlıdır
        self.setAttribute(Qt.WA_DeleteOnClose)
        
        izgara = QGridLayout()
        izgara.addWidget(QLabel('Yazı Tipi'), 0,0,1,1)
        
        self.yaziTipiListe = QFontComboBox()  #otomatik yazı tipi çıkarıyor
        self.yaziTipiListe.setCurrentFont(QFont(self.parent.yaziTipi))
        izgara.addWidget(self.yaziTipiListe, 0,1,1,1)
        
        dugmeKutusu = QDialogButtonBox(QDialogButtonBox.Ok|
                                       QDialogButtonBox.Apply|
                                       QDialogButtonBox.Reset|
                                       QDialogButtonBox.Cancel)
        dugmeKutusu.button(QDialogButtonBox.Ok).setText('Tamam')
        dugmeKutusu.button(QDialogButtonBox.Cancel).setText('Vazgeç')
        dugmeKutusu.button(QDialogButtonBox.Apply).setText('Uygula')
        dugmeKutusu.button(QDialogButtonBox.Reset).setText('Sıfırla')
        
        
        dugmeKutusu.button(QDialogButtonBox.Ok).clicked.connect(self.kabul)
        dugmeKutusu.button(QDialogButtonBox.Cancel).clicked.connect(self.iptal)
        dugmeKutusu.button(QDialogButtonBox.Apply).clicked.connect(self.uygula)
        dugmeKutusu.button(QDialogButtonBox.Reset).clicked.connect(self.sifirla)
        izgara.addWidget(dugmeKutusu,1,0,1,2)
        
        self.setLayout(izgara)
        self.setWindowTitle('Yazı Tipini Ayarla')
        self.setWindowIcon(QIcon("roket.jpg"))
        
        
    def kabul (self):
        self.parent.yaziTipi = self.yaziTipiListe.currentFont().family()
        self.parent.etiket.setText(self.parent.metin % self.parent.yaziTipi)
        QDialog.accept(self)
        
        
    def uygula (self):
        self.parent.etiket.setText(self.parent.metin % self.yaziTipiListe.currentFont().family())
        
    
    def sifirla (self):
        self.parent.etiket.setText(self.parent.metin % self.parent.yaziTipi)
        self.yaziTipiListe.setCurrentFont(QFont(self.parent.yaziTipi))
        
    def iptal (self):
        self.parent.etiket.setText(self.parent.metin % self.parent.yaziTipi)
        QDialog.reject(self)
        
        
            
class AnaUygulamaAkilliDiyalog (QDialog):
    def __init__(self, parent=None):
        super(AnaUygulamaAkilliDiyalog,self).__init__(parent)
        self.yaziTipi = 'Verdana'
        self.metin = '<font color ="black" face="%s" size ="+3"> gorsel programlama dersi</font>'
        self.etiket = QLabel(self.metin % self.yaziTipi)
        
        kutu = QVBoxLayout()
        kutu.addWidget(self.etiket)
        
        yaziTipiDugme = QPushButton("Yazı Tipini Değiştir")
        yaziTipiDugme.clicked.connect(self.yaziTipiDegistir)
        kutu.addWidget(yaziTipiDugme)
        self.setLayout(kutu)
        self.setWindowTitle("Ana Uygulama")
        self.setWindowIcon(QIcon("roket.jpg"))
        
        
    def yaziTipiDegistir(self):
        diyalog = yaziTipiDiyalog2(self)
        diyalog.exec_()               
        
uyg = QApplication([]) 
pencere = AnaUygulamaAkilliDiyalog() 
pencere.show()
uyg.exec_()            
