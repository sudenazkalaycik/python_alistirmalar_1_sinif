#Fonksiyon kullanılarak yapılan bst hesap makinesi

def toplama(x,y):
    return x+y
    

def cikarma(x,y):
    return x-y
    

def carpma(x,y):
    return x*y

def bolme(x,y):
    if y!=0:
        return x/y
    else:
        return "Bölüm 0 değerini alamaz"
    
def us_alma(x,y):
    return x**y

def karekok(sayi):
    return sayi**(1/2)


def menu():
    print(""" 
Yapmak istediğiniz işlemi seçiniz
$toplama için: +
$çıkarma için: -
$bölme için: /
$çarpma için: *
$üs alma için: ^
$karekök için: **
          """)

    islem=input(">>")
     
    if islem=="**":
        sayi=float(input("Sayı değeri giriniz: "))
        sonuc= karekok(sayi)
        print(sonuc)
        
        
    else:
        x=float(input("Sayı değeri giriniz: "))
        y=float(input("Sayı değeri giriniz: ")) 

        
        if islem =="+":
            sonuc= toplama(x,y)
        elif islem== "-":
            sonuc= cikarma(x,y)
            
        elif islem=="*":
            sonuc= carpma(x,y)
            
        elif islem=="/":
            if y!=0:
                sonuc=bolme(x,y)
            else:
                print("Sayıyı sıfıra bölme işlemi tanımsızdır.")
        
        elif islem=="^":
            sonuc= us_alma(x,y)
        
        else:
            print("Hatalı giriş yaptınız.")
        
        print(sonuc)

while True:
    menu()   #fonksiyonu çağırırken print yazmamıza gerek yok eğer print(menu()) şeklinde yazarsak sonuca ek olarak None değerini de döndürüyor.    



