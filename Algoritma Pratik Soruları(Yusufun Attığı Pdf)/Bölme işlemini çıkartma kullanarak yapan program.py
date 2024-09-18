#Bölme işlemini çıkartma kullanarak yapan program
bolum_ifadesi=0
sayi1= int(input("Bölmek istediğiniz değeri giriniz: "))
sayi2= int(input("Bölecek sayıyı giriniz: "))
while sayi1>sayi2:
    sayi1= sayi1-sayi2
    bolum_ifadesi+=1
print("Bölüm:", bolum_ifadesi)
print("Kalan:", sayi1)    

