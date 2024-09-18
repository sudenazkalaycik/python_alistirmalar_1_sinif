#Listede en fazla tekrar eden elemanı silen program

def en_cok_tekrar_edeni_sil(liste):
    en_cok_tekrar_sayisi = 0
    en_cok_tekrar_eden = None  #bir değer atamadık 

    for i in range(len(liste)): # liste uzunluğu kadar gezinsin
        eleman = liste[i]  # i. indeksteki elman değerini eleman değişkenine atar.  
        tekrar_sayisi = 1    

        for j in range(i + 1, len(liste)): # index+1 den liste uzunluğuna kadar gezinsin burası her defasında bir index atladığı için asıl kontrol kısmı burası
            if eleman == liste[j]:
                tekrar_sayisi += 1
 
        if tekrar_sayisi > en_cok_tekrar_sayisi:
            en_cok_tekrar_sayisi = tekrar_sayisi
            en_cok_tekrar_eden = eleman

    temizlenmis_liste = [eleman for eleman in liste if eleman != en_cok_tekrar_eden]

    return temizlenmis_liste


ornek_liste = [1, 2, 3, 2, 4, 2, 5, 6, 2, 7]
temizlenmis_liste = en_cok_tekrar_edeni_sil(ornek_liste)

print("Orjinal Liste:", ornek_liste)
print("Temizlenmiş Liste:", temizlenmis_liste)

