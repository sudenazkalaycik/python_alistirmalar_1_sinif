#Girilen sayının mükemmel sayi olup olmadığını kontrol eden program
# (kendisi hariç pozitif bölenler toplamı kendine eş ise mük sayidır)
sayi =int(input("Sayi giriniz:"))
ptbs=0
for i in range(1,sayi):
    if sayi%i==0:
        ptbs+=i
        if ptbs==sayi:
            print("Mükemmel sayıyı buldun.")
        else:
            print("Battın knk")
  