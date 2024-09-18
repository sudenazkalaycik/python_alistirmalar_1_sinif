#Girilen sayının 5' in kuvveti olup olmadığını kontrol eden program
sayi= int(input("Sayı giriniz: "))
if sayi%5==0:
    while sayi>=5:
        sayi=sayi/5
    if sayi==1:
        print("5'in katı")
    else:
        print("5'in katı değil.")
else:
    print("5'in katı değil.")

