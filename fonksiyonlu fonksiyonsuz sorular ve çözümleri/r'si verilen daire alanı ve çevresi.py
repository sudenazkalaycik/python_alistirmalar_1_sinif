#Yarıçapı dışarıdan verilen dairenin çevresini ve alanını bulan program
r=int(input("Yarıçap değeri giriniz: "))
pi= 3.14
daire_cevre= pi*2*r
daire_alan=pi*r**2 # ya da pi*r*r kullanılabilir
print(f"Yarıçapı {r} olan dairenin alanı {daire_alan}'dır.")
print(f"Yarıçapı {r} olan dairenin çevresi {daire_cevre}'dır.")