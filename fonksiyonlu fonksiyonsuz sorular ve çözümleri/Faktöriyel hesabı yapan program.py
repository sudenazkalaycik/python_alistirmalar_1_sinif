 #Faktöriyel hesabı yapan program
sayi=int(input("Sonucunu istediğiniz faktöriyeli giriniz:"))
fak=1
for i in range(sayi):
    if sayi>0:
        fak*=sayi
        sayi-=1
        
print(f"Sonuç: {fak}")