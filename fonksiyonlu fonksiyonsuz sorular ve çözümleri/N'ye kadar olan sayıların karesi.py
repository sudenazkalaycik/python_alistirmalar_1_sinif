#N sayısına kadar olan sayıların karelerinin toplamını bulan program
toplam=0
N=int(input("N sayı değerini giriniz: "))
for i in range(N):
    toplam+=i**2
print(f"N'ye kadar olan sayıların kareler toplamı {toplam}")
