#Girilen N sayısının asal olup olmadığını bulan program
a=int(input("Değer girini:"))
# asal sayılar sadece kendilerine ve 1'e tam bölünürler.Bu yüzden döngüyü 2 den başlattık. Ayrıca başlangıç değeri vermediğimde 
#"ZeroDivisionError: integer modulo by zero" (sıfıra bölünme) hatası alıyorum. 
for i in range(2,a): 
    if a%i==0:
        print(f"{a} sayısı asal DEĞİLDİR!")
        break
    else:
        print(f"{a} sayısı asaldır.")
        break