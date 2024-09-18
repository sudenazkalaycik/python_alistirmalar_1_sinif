#2 kenarı verilen dik üçgenin 3. kenarını bulan program
kenar1=int(input("1. kenar değerini giriniz:"))
kenar2=int(input("2. kenar değerini giriniz:"))
kenar3_karesi= kenar1**2 + kenar2**2
#kütüphaneye ihtiyaç duymamak adına kök derecesini üstlü sayı şeklinde yazıp üs alma işlemi yaparak 3. kenarın değerine ulaşabiliriz.
kenar3= kenar3_karesi**(1/2) 
print(f"3. kenar {kenar3}'dir.")

#NOT: karekök= üs olarak (1/2) yazılır aynı şekilde n. dereceden bir kök ise üs olarak (1/n) olarak yazılır. 