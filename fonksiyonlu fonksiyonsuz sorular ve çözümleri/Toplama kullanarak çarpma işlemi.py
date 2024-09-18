#Çarpma işlemi kullanmadan iki sayının çarpımını bulan program

#while döngüsü ile
print("Çarpılacak sayıları giriniz:")
sayi1=int(input(">>"))
sayi2=int(input(">>"))
sayac=0
sonuc=0
while sayac<sayi2:
    sonuc+=sayi1
    sayac+=1
print("Sonuç:",sonuc)


#for döngüsü ile
print("Çarpılacak sayıları giriniz:")
sayi1=int(input(">>"))
sayi2=int(input(">>"))
toplam=0
for i in range(sayi2):
    toplam+=sayi1
print("Sonuç:",toplam)
