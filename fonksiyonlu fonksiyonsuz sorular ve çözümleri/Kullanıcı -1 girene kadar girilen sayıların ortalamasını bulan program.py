#Kullanıcı -1 girene kadar girilen sayıların ortalamasını bulan program
toplam=0
print("BİLGİ:'-1' değeri girdiğinizde veri giriiş işlemi sonlanacak ve toplama sonucu verilecektir.")
print("Sayı değerini giriniz:")
while True:
    sayi=int(input(">"))
    if sayi!=-1:
        toplam+=sayi
    else:
        break 
print(f"Toplam: {toplam}")    