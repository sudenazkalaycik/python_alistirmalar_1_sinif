#girilen değer ile istenilen değerin modunu alan(bölümden kalanını alan) program
ilk_deger= int(input("Modu alınacak sayıyı giriniz: "))
ikinci_deger=int(input("Modu olacak sayıyı giriniz: "))
sonuc= ilk_deger%ikinci_deger
print(sonuc)

#mod (%) kullanmadan nasıl yapardık?
kalan_mod=0
bolum_degeri=0
sayi1=int(input("Bölünecek sayıyı giriniz: "))
sayi2=int(input("Bölecek sayıyı giriniz: "))
while sayi1>=sayi2:
    sayi1=sayi1-sayi2
    bolum_degeri+=1
    kalan_mod= sayi1
print(kalan_mod)