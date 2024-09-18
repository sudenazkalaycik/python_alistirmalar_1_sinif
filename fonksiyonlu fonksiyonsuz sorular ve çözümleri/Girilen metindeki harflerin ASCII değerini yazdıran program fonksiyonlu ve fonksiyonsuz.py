#Girilen metindeki harflerin ASCII değerini yazdıran program

# ord() fonksiyonu karakterin ascii değerini döndürür.
# işlem yapılırken aynı karakterde birden fazla olabilir, biz her bir farklı karakteri sadece 1 kez yazdırmak istiyoruz.



metin=input("Metin girişi yapınız: ")
#metindeki her karakterin 1 kez kullanılmasını sağlayalım
duzenlenmis_metin=""
for i in metin:
    if i not in duzenlenmis_metin:
        duzenlenmis_metin+= i

#ascii karakterlerini yazdıralım

for karakter in duzenlenmis_metin:
    ascii= ord(karakter)
    print(f'{karakter}={ascii}', end=" ")

#def ile deneyelim


#buradaki parantezler arasına yazdığın şeylerin bir anlamı yok onlar eğişkenlerdir. Fonksiyonu kullanmak istediğinde oraya gereken bilgiyi gireceksin.
#fonksiyonu yazarken def ornek(x): şeklinde oluşturduk diyelim ve fonksiyon bloğu içerisinde x li bir sürü işlem var. Burada x in ne olduğunun bir önemi yok
# sen fonksiyonu çağırıp kullandığında x yerine gereken parametreyi gireceksin zaten. 

def metin_karakterleri(metin): 
    duzenlenmis_metin=""
    for karakter in metin:
        if karakter not in duzenlenmis_metin:
            duzenlenmis_metin += karakter
    return duzenlenmis_metin


def ascii_cevirme(x):
    for i in x:
       ascii= ord(i)
       print(f"{i}={ascii}", end=" ")  #buaraya return kullanmak için başka bir formda yazman gerek, ayrıca return için liste kullanmak daha mantıklı :)




metin=input("Metin giriniz: ")
ascii_cevirme(metin_karakterleri(metin))  
#burada ascii_cevirme(x) fonksiyonunda x parametresine metin_karakter() fonksiyonunu atadım. metin_karakter fonksiyonunun içerisine ise metin degerini atadım. Eğer 
# metin_karakter(metin) değil de metin_karakter(y) yazıp kod bloğunun içindeki işlemlerde de metin yerine y kullansaydım kodum yine doğru olurdu. Ben fonksiyonu
#çağırdığımda y parametresine metin değerini atayacaktım ve kod çalışacaktı. KISACASI KODU OLUŞTURURKEN FONKSİYON() PARAMERESİNE NE YAZDIĞININ ÖNEMİ YOK. Çağırdığında
#ne yazdığın önemli.
    

