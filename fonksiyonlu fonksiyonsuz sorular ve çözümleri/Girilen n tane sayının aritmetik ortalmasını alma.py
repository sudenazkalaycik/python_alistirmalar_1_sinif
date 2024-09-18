#Girilen N tane sayının aritmetik ortalamasını bulan program
n=int(input("""Kaç sayı gireceksiniz? """))
sayac=0
toplam=0
print("Sayıları giriniz.")
while sayac<n:
    i=int(input(">>"))
    toplam+=i
    sayac+=1
aritmetik_ortalama= toplam/n
print(f"Girdiğiniz sayıların aritmetik ortalamsı {aritmetik_ortalama}'dır.")