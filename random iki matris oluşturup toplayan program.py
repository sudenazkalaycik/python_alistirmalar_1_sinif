def fonksiyon_yazdırma(Matrisİsmi, Matris ):
    print(Matrisİsmi)  #matris nasıl yazılır
    for i in range(len(Matris)):
        for j in range(len(Matris[0])):
            print(Matris[i][j], end=" ")
        print() 
        


def toplamaFonksiyonu(Matris1, Matris2):
    liste=list()
    for i in range (len(Matris1)):
        satir=list()
        for j in range (len(Matris1[0])):
            toplam= Matris1[i][j] + Matris2[i][j]
            satir.append(toplam)
        liste.append(satir)
    return liste


def teksatirdaToplamaFonksiyonu():
    import random
    m= int(input("Matris boyutunu gitiniz(kare matris, bu yüzden tek değer girmeniz yeterlidir): ")) # girilen boyutta kare matrisler oluşturmak istiyoruz 
    Matris1=[[random.randint(1,9) for i in range(m)] for j in range(m)],
    Matris2=[[random.randint(1,9) for i in range (m)] for j in range(m) ]
    SonucMatrisi=[[0 for i in range(m)]  for j in range(m)]
    print(Matris1)
    print()
    print(Matris2)
    print()

    for i in range(m):
        for j in range(m):
            SonucMatrisi[i][j]= Matris1[i][j] + Matris2[i][j]




