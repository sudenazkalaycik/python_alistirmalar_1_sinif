#klavyeden girilen 20 sayıdan çif ve tek sayıların kendi içlerinde toplamlarının oranını veren program
# random sayi üretimi için "import random" tanımla
girilen_sayilar= 0
cift_toplam=0
tek_toplam=0
liste=[]
while girilen_sayilar<20:
    sayi=int(input("Sayi girin: ")) #bunu satırın yerine "sayi=random.randint(0,300) #parantez içi aralık belirliyor. " yaz (random sayi için)
    liste.append(sayi)
    girilen_sayilar+=1
    
for i in liste:
    if i%2 ==0:
        cift_toplam+=i
    else:
        tek_toplam+=i    
            
if tek_toplam !=0:    
    oran= cift_toplam/tek_toplam
    print("Çift sayılar toplamı: ",cift_toplam)
    print("Tek sayılar toplamı: ", tek_toplam)
    print("Çift sayıların tek sayılara oranı", oran)   
else: 
    print("Girilen tek sayi değerleri toplamı paydayı 0 yaptığı için değer hesaplanamıyor.")