#N tam sayısına kadar olan tek ve çift sayıların toplamını veren program
cift_toplam=0
tek_toplam=0
N=int(input("N değeri giriniz: "))
for i in range(N):
    if i%2==0:
        cift_toplam+=i
    else:
        tek_toplam+=i

print(f"Tek sayılar toplamı {tek_toplam}")
print(f"Çift sayılar toplamı {cift_toplam}")