#fibonacci serisinin ilk 10 terimi
sonraki=1
baslangic=1
print(baslangic)
print(sonraki)
for i in range(8):
    sonuc=baslangic+sonraki
    print(sonuc)
    sonraki=baslangic
    baslangic=sonuc