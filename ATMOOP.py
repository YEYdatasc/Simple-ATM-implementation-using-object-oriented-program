class Musteri:
    def __init__(self,ad,soyad,kartsifre,hesapbakiye,kredikartborc,sonodeme):
        self.ad=ad
        self.soyad=soyad
        self.kartsifre=kartsifre
        self.hesapbakiye=hesapbakiye
        self.kredikartborc=kredikartborc
        self.sonodeme=sonodeme
Ahmethesap=Musteri("Ahmet","Candan","1357",5000,4200,"20/11/2021") 
Mehmethesap==Musteri("Mehmet","Duyar","2468",6000,3800,"28/11/2021") 
Takılankart=Ahmethesap


class ATM:
    def __init__(self,atmad):
        self.atmad=atmad
        self.giriskontrol()
        self.dongu=True
    def giriskontrol(self):
        Hak=2
        for i in range(0,3):
            Sifre=input("Lütfen 4 Haneli Şifrenizi Giriniz:")
            if Sifre==Takılankart.kartsifre:
                self.program()
            elif Sifre!=Takılankart.kartsifre and Hak!0:
                print("Hatalı Şifre Girdiniz. Kalan Hakkınız {}".format(Hak))
                Hak-=1
            elif Sifre!=Takılankart.kartsifre and Hak==0:
                print(""""Şifrenizi 3 defa Hatalı Girdiğinizden Dolayı Kartınız Bloke Olmuştıur.
                      Lütfen En Yakın Şubemize Başvurunuz!!!""")
                exit()
    def program(self):
        secim=self.menu()
        
        if secim==1:
            self.bakiye()
        if secim==2:
            self.kkborc()
        if secim==3:
            self.paracek()
        if secim==4:
            self.parayatır()
        if secim==5:
            self.cıkıs()
            
    def menu(self):
        secim=int(input("****Merhabalar, {}'a Hoşgeldiniz Sayın {} {}.\n\nLütfen Yapmak İstedğiniz İşlemi Seçiniz...\n\n[1] Bakiye Sorgulama\[2]Kredi Kartı Borç Sorgulama\n[3]  Para Çekme\n[4]  Para Yatırma\n[5] Kart İade\n\nSeçim:".format(self.atmad,Takılankart.ad,Takılankart.soyad)))
        
        
    def bakiye(self):
        print("Hesap Bakiyeniz: {} TL'dir.".format(Takılankart.hesapbakiye)) 
        while secim<1 or secim>5:
            print("\n\nLütfen 1 ve 5 Arasında Geçerli Bir Değer Giriniz...\nAna Menüye Dönülüyor..."
            self.program())
            
        return secim
        
        
    def kkartborc(self):
    
    def paracek(self):
        pass
    def parayatır(self):
        pass
    def cıkıs(self):
        pass
    def menudon(self):
        pass
    
Banka=ATM("XBank")
while Banka.dongu:
    Banka.program()
    
    
         
                  
    
    
    
    
    
    
    
    
    
    
    
    
    
    