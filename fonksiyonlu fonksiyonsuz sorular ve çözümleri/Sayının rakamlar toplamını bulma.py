#Girilen N sayısının rakamlarının toplamını bulan program
sayi=int(input("Sayı gir:"))
toplam=0
while sayi>0:
    rakam=sayi%10  #mod alarak sayının en sağındaki sayıya ulaştım
    toplam+=rakam  #rakamı toplam değere ekledim
    sayi-=rakam    #sayıdan rakamı çıkarıp birler basamağını sıfırladım
    sayi/=10       #sonra en sağdaki 0'dan kurtularak sayıyı bi basamak eksilttim
print("Girilen sayıların rakamları toplamı:", toplam)