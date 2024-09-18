#N sayısına kadar olan sayıların toplamını veren program
N=int(input("Bir değer belirleyiniz: "))
toplam=0
for i in range(N):
     toplam+=i
print(toplam)