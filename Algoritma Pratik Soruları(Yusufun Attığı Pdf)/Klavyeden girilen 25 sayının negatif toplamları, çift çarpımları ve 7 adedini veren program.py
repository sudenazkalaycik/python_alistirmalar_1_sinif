#Klavyeden girilen 25 sayının negatif toplamları, çift çarpımları ve 7 adedini veren program
#(eğer random sayi girişi istersen import ve ramdom komutunu yorum satırından çıkarıp input kısmını yorum satırına al.)

#import random
liste=[]
sayi=0
while sayi<25:
    #sayi_giris= random.randint(-567,156)
    sayi_giris= int(input("Sayi giriniz: "))
    liste.append(sayi_giris)
    sayi+=1

print(liste)

negatif_toplam=0
cift_carpim=1
yedi_sayisi=0
for i in liste:
    if i<0:
        negatif_toplam+=i
    elif i%2==0:
        cift_carpim*=i
    elif i ==7:
        yedi_sayisi+=1

print( "Negatif sayılar toplamı: ", negatif_toplam)
print( "Çift sayıların çarpımı: ", cift_carpim)
print( "Girilen sayılarda bulunan 7 adedi: ",yedi_sayisi)

