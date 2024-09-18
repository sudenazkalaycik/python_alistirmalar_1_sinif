#Dışarıdan girilen 3 sayının en büyüğünü bulan program
en_buyuk=0  #negatif sayılar girilirse program patlar :)
sayac=0
print("Karşılaştırılacak olan sayı değerlerini giriniz:")
while sayac<3:
    i=int(input(">>"))
    if en_buyuk<i:
        en_buyuk=i
    sayac+=1
print(f"Girilen sayıların en büyüğü {en_buyuk}'dir.")