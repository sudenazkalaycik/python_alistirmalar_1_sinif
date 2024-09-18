#random matris oluşturu
import random
matris_liste= []
satir=int(input("Satır değeri giriniz:"))
sutun=int(input("Sütün sayısı giriniz:"))

for i in range(satir): #satır elemanı kadar dönsün
    satir_liste=[]
    for j in range(sutun): 
        satir_liste.append(random.randint(1,10))
    matris_liste.append(satir_liste)

#matrisi oluşturduk şimdi ise yazdırmamız gerek

for i in range (len(matris_liste)):
    for j in range(len(matris_liste[0])):
        print(matris_liste[i][j], end="")
    print()
    
    
    

        



        
