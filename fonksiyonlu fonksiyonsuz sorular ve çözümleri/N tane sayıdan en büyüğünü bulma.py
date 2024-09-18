#N kez dışarıdan sayı alıp aldığı sayıların en büyüğünü bulan program
N=int(input("""Kaç adet sayı gireceksiniz? :"""))
sayac=0
en_buyuk=0
print("Sayıları giriniz:")
while sayac<N:
    i=int(input(">>"))
    if i > en_buyuk:
        en_buyuk=i
    sayac+=1
print(f"Girilen sayıların en büyüğü {en_buyuk}'dir.")