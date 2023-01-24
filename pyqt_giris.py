# -*- coding: utf-8 -*-


#Her QT uygulaması QApplication nesnesinden oluşur.
#Bu nesne, içerisine aktarılacak argümanları alır.
#Parametreler, QApplication nesnesine bir liste veya tüp olarak verilir.
# Alttaki kod parçasında QApplication nesnesine herhangi bir argüman aktarılmadan 
# boş liste verildi.
# Widget, parçacık anlamındadır. Alttaki kod satırında bir etiket parçacığı oluşturuldu
# Ve show() fonksiyonu ile görünür yapıldı. 
# Son olarak uygulama exec_() komutu ile başlatılmıştır.
# Bu satır GUI (Graphical User Interface) terminolojisinde 'uygulama döngüsü'
# olarak isimlendirilir. 
# Her GUI uygulaması sürekli bir döngüyü ifade eder.
# Böylelikle parçacıklar üzerindeki fare yada klavye hareketleri
# yakalanarak yapılması gerekenler işleme sokulur.
# Klavye, fare yada başka bir cihaz üzerinden GUI üzerindeki hareketler 
# event (olay) olarak adlandırılır.
# Bu sebeple exec_() döngüsüne 'olay döngüsü' de denilir. 
# Aşağıdaki kod satırının bu anlamda geliştirilmeye ihtiyacı vardır.
# Çünkü, kullanıcıdan gelecek herhangi bir etkiye cevap verebilecek bir denetim
# içermemektedir.
# Oysa bir GUI uygulaması olay döngüsü başladığı andan itibaren kullanıcıdan 
# gelecek olan etkilere tepki vermek üzere bekler. 
# Ve pencere kapatılana kadar (kullanıcı tarafından yada yazılımsal) 
# döngü devam eder. 


"""
from PyQt5.QtWidgets import *

uyg = QApplication([])
etiket = QLabel("görsel programlama ")
etiket.show()
uyg.exec_()

"""


# Etiketler HTML ile tasarlanabilir:
    
"""
from PyQt5.QtWidgets import *

uyg = QApplication([])
etiket = QLabel('< font color ="blue", size = "+3" > görsel programlama</font>'  )
etiket.show()
uyg.exec_()

"""


# Pencere Düzenleri

# Bir GUI uygulamasında genelde birden fazla pencere oluşur.
# Ve her pencerede birden fazla parçacık bulunur.
# Önceki yazdıklarımızda sadece bir parçacık olduğundan pencere düzeni
# kullanılmamıştı.
# Pencere düzenleri ya kutularla yada ızgaralarla oluşturulur.
# Birlikte de kullanılabilirler.
# Kutular iki türlü tasarlanabilir:
# dikey kutular (QVBoxLayout) ve yatay kutular(QHBoxLayout)
# Bir kutuya parçacık eklemek için addWidget() özelliği kullanılır.
# Bunun için öncelikle QWidget oluşturmalıyız:
    

# Kutularla pencere düzeni:
    
    
"""
from PyQt5.QtWidgets import *

uyg = QApplication([])
pencere = QWidget()
etiket = QLabel('< font color ="blue", size = "+3" > görsel programlama  </font>' )
dugme = QPushButton('Tıkla') # Bastırılabilen düğme
kutu = QVBoxLayout()
kutu.addWidget(etiket)
kutu.addWidget(dugme)
pencere.setLayout(kutu)
pencere.setWindowTitle("Konu Hakkında")
pencere.show()
uyg.exec_()

"""

# PYQT Sinyalleri

# Kullanıcı etkileşimi sonucu oluşan sinyallerdir. 
# Örneğin: Farenin bir tuşuna tıklamak veya klavyeden bir tuşa basmak.
# Örnek: Kullanıcı QPushButton düğmesine bastığında clicked üzerinden güncelleme olur.
# Kullanıcılar programı kullanırken bu gibi birçok sinyal üretilir.
# Bizler bu sinyalleri yayınlayan nesnelere bağlantı kurup bir fonksiyona (işleve)
# yönlendirirsek GUI uygulamamız iş yapacaktır.
# Qt'de sinyallerin bağlandığı fonksiyonlar 'slot' yada 'yuva' olarak adlandırılır.
# Aşağıdaki örnek kod parçasını inceleyiniz:

"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def metinGuncelle():
    print ("Düğmeye basıldı")
    
def metinGuncelle2():
    etiket.setText ('< font color ="red", size = "+3" > Dugmeye Bas</font>')

uyg = QApplication([])
pencere = QWidget()
etiket = QLabel('< font color ="blue", size = "+3" > görsel programlama </font>' )
dugme = QPushButton('Tıkla') # Bastırılabilen düğme
dugme.clicked.connect(metinGuncelle2)
kutu = QVBoxLayout()
kutu.addWidget(etiket)
kutu.addWidget(dugme)
pencere.setLayout(kutu)
pencere.setWindowTitle("Konu Hakkında")
pencere.show()
uyg.exec_()

"""



# Pyqt Sınıfları

# GUI uygulamasını daha modüler ve okunabilir hale getirmek için sınıflar ile
# tasarım yapılmalıdır:
    
"""    

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class guiUygulama (QDialog):
    def __init__(self, parent=None):
        super(guiUygulama,self).__init__(parent)
        self.etiket = QLabel('< font color ="blue", size = "+5" > PyQt Sınıfları Hakkında </font>')
        dugme = QPushButton('Tıklayınız')
        dugme.clicked.connect(self.metinGuncelle2)
        kutu = QVBoxLayout()
        kutu.addWidget(self.etiket)
        kutu.addWidget(dugme)
        self.setLayout(kutu)
        self.setWindowTitle("görsel programlama ")
        self.resize(300, 400)
        self.move(200,50) # 0 0 konumu sol üst köşedir. ilk argüman yatay; ikinci argüman dikey uzaklıktır.
        
    def metinGuncelle2(self):
        self.etiket.setText ('< font color ="red", size = "+3" > Dugmeye Basıldı</font>')   
    
        
uyg = QApplication([])
pencere = guiUygulama()
pencere.show()
uyg.exec_()

"""

# Yukarıdaki sınıfta parent = None olarak verilmiştir.
# Bunun sebebi yazdığımız sınıfın başka bir sınıfa bağlı olmamasıdır.
# Parent-child ilişkisi düzgün belirlenmelidir
# Bu durum düzgün tasarlanamazsa parente bağlı ana pencere kapatılınca
# child sınıfta açık pencerenin kalması yada sınıfların birbirini istenmeyen şekilde
# etkilemesi söz konusu olabilir.  


# Bundan önceki örneklerde kutularla tasarım yapıldı
# Dikey kutuda eklenilen widget yani parçacıklar dikey olarak alt alta dizilmişti.  
# Izgara pencere düzeninde ise mekanizma şu şekildedir:    
# Qt parçacıkları tablo üzerine yerleştirilir gibi kullanılır.
# addWidget (parçacık, satır, sütun, satırGenişliği, sütunGenisliği)   
# parçacık: parçacık ismi, etiket düğme gibi
# satır: hangi satırın eklenecek ve
# Sütun: hangi sütununa 
# satırGenisliği: kaç satıra
# kaç sütuna yayılacak 
# bilgisidir.    


#METİN BÜYÜLTME VE KÜÇÜLTME**************

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class guiUygulama2 (QDialog):
    def __init__(self, parent=None):
        super(guiUygulama2,self).__init__(parent)
        self.boy = 3
        self.metin = '<center><font color ="blue" size ="+%d"> görsel programlama </font></center>'
        self.etiket = QLabel(self.metin % self.boy)
        dugmeKucult = QPushButton('Metni Küçült')
        dugmeKucult.clicked.connect(self.metinKucult)
        dugmeBuyut= QPushButton("Metni Büyüt")
        dugmeBuyut.clicked.connect(self.metinBuyut)
        izgara = QGridLayout()
        izgara.addWidget(self.etiket, 0,0,1,2)
        izgara.addWidget(dugmeKucult,1,0,1,1)
        izgara.addWidget(dugmeBuyut,1,1,1,1)

        self.setLayout(izgara)
        self.setWindowTitle('PyQt Izgarası')
        self.resize(500, 100)
    
    def metinBuyut (self):
        if self.boy <=4:
            self.boy = self.boy + 1
            self.etiket.setText(self.metin % self.boy) 
            print (self.boy)
            
    def metinKucult(self):
        if self.boy >= 1:
            self.boy = self.boy - 1
            self.etiket.setText(self.metin % self.boy) 
            print (self.boy)
        
        
uyg = QApplication([])     
pencere = guiUygulama2()
pencere.show()
uyg.exec_()