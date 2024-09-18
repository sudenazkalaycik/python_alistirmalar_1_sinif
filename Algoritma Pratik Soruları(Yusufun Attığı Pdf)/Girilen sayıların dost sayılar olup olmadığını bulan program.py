# Girilen sayıların dost sayılar olup olmadığını bulan program
# bir sayısının çarpanları toplamı diğer sayının kendisine eşit ise ve aynı şey karşılıktı olarak geçerli ise buna dost sayılar denir.
#while döngüsüyle:

sayi_x=int(input("X sayısı için değer giriniz: "))
sayi_y=int(input("Y sayısı için değer giriniz: "))
i=1 
carpan_toplamlar_x=0
carpan_toplamlar_y=0
while sayi_x>i:
    if sayi_x%i==0:
        carpan_toplamlar_x+=i
        i+=1
    else:
        i+=1
print(carpan_toplamlar_x)

i=1
while sayi_y>i:
    if sayi_y%i==0:
        carpan_toplamlar_y+=i
        i+=1
    else:
        i+=1
print(carpan_toplamlar_y)

if carpan_toplamlar_y==sayi_x and carpan_toplamlar_x==sayi_y:
    print("Girilen sayılar dost sayılardır.")
else :
    print("Girilen sayılar dost sayı DEĞİLLERDİR.")
    
#220 ve 284, 1184 ve 1210, 5020 ve 5564 sayıları kullanılarak test edilebilir bu sayı çiftleri dost sayılardır.

#for döngüsüyle:

sayi_x = int(input("X sayısı için değer giriniz: "))
sayi_y = int(input("Y sayısı için değer giriniz: "))

carpan_toplamlar_x = 0
carpan_toplamlar_y = 0

for i in range(1,sayi_x):
    if sayi_x % i == 0:
        carpan_toplamlar_x += i

print(carpan_toplamlar_x)

for i in range(1,sayi_y):
    if sayi_y % i == 0:
        carpan_toplamlar_y += i

print(carpan_toplamlar_y)

if carpan_toplamlar_y == sayi_x and carpan_toplamlar_x == sayi_y:
    print("Girilen sayılar dost sayılardır.")
else:
    print("Girilen sayılar dost sayı DEĞİLLERDİR.")
