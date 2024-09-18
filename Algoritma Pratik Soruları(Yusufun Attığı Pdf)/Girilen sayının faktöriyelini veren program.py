#girilen sayının faktöriyelini verir
sayi= int(input("Faktöriyel alınmasını istediğiniz sayıyı giriniz: "))
fakt= 1 
while sayi>1 :
   fakt= fakt*sayi
   sayi-=1
print(fakt)