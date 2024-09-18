# 3 basamaklı sayının basamaklarının küpler toplamı kendine eşit mi değil mi yi veren program
sayi= int(input("3 basamaklı bir sayı giriniz: "))  #Doğruluğu test etmek için 153 değeri verebilirsin.
yuzler = sayi//100
deger = sayi-yuzler*100
onlar = deger//10
birler = deger - onlar*10

kup_toplami= yuzler**3 + onlar**3 + birler**3
if kup_toplami== sayi:
    print("Girilen sayı ile sayı basamaklarının küpler toplamı eşittir.")
else:
    print("Sayı ile basamaklarının küpler toplamı eşit DEĞİLDİR!") 