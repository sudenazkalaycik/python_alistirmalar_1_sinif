#Basit hesap makinası programı
islem_sec=input("""Yapmak istediğiniz işlemi seçiniz:

>Toplama
>Çıkarma
>Çarpma
>Bölme 
>Üs Alma 
>Karekök
""")

if islem_sec=="Toplama" or islem_sec=="toplama":
    toplam=0
    n=int(input("Kaç sayı ile işlem yapcaksınız? "))
    sayac=0
    print("İşlem yapmak istediğniz sayıları giriniz")
    
    while n>sayac:
        sayi=int(input(">"))
        toplam+=sayi
        sayac+=1
        
    print(f"Sonuç: {toplam}")
    
    
elif islem_sec=="Çıkarma" or islem_sec=="çıkarma":
    n=int(input("Kaç sayı ile işlem yapacaksınız? "))
    sayac=0
    print("İşlem yapmak istediğiniz sayıları giriniz")

    a= int(input(">"))
    while sayac<n-1 :
        sayi=int(input(">"))
        a-=sayi
        sayac+=1
    print(f"Sonuç {a}")
    
            
elif islem_sec=="Çarpma" or islem_sec=="çarpma" :
    n=int(input("Kaç sayı ile işlem yapacaksınız? "))
    sayac=0
    carpim=1
    print("İşlem yapmak istediğiniz sayıları giriniz")
    while sayac<n:
        sayi=int(input(">"))
        carpim*=sayi
        sayac+=1
    print(f"Sonuç: {carpim}")

elif islem_sec=="Bölme" or islem_sec=="bölme":
    n=int(input("Kaç sayı ile işlem yapacaksınız? "))
    sayac=0
    print("işlem yapmak istediğiniz sayıları giriniz")
    a=int(input(">"))
    while sayac<n-1:
        sayi=int(input(">"))
        a/=sayi
        sayac+=1   # her bölme adımından sonra sonucu görmek istersen printi döngü içine alabilirsin
    print(f"Sonuç: {a}")
        


elif islem_sec=="Üs Alma" or islem_sec=="üs alma":
    print("İşlem yapmak istediğiniz sayıları giriniz")
    taban=int(input("Taban değeri giriniz:"))
    us=int(input("Kuvvet(üs) değeri giriniz:"))
    islem= taban**us
    print(islem)

elif islem_sec=="Karekök" or islem_sec=="karekök":
    print("İşlem yapmak istediğininiz sayıyı giriniz ")
    sayi=int(input(">"))
    karekok= sayi**(1/2)
    print(karekok)
    


else:
    print("Hatalı giriş yaptınız")
   
                

            