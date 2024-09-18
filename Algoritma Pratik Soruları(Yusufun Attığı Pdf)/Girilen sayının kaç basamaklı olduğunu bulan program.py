#Girilen sayının kaç basamaklı olduğunu bulan program
kontrol= 1
sayi= float(input("Sayı giriniz: "))
while sayi>9:
    sayi= sayi/10
    kontrol+=1
print(kontrol)

#length komutu kullanarak basamak sayısını string tipinde bulan kod (diğer yöntem daha sağlıklı)
sayi= (input("Sayı giriniz: "))
print(len(sayi))

