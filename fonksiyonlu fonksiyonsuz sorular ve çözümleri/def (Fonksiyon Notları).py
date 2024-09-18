# çoğunlukla fonksiyonların içine print yazılmaz çünkü yapmak istediğimiz her işlemde daima ekrana yazdırma amacı gütmeyiz.


#return e yazılan her şey fonksiyona eşitlenir. Yani ben her fonksiyonu çağırdığımda o eşitlik karşıma çıkar. Örneğin x=5 dersem x e 5 değerini atamış olurum
# ve ben her x değerini kullandığımda karşıma 5 değeri çıkar yanı x her zaman 5 değeri döndürür. Return komutu da aynısını yapar. Eğer ben

#def us_alma_islemi(taban,us):
    #sonuc=taban**us
    #return sonuc 
#gibi bir fonksiyon oluşturur ve fonksiyonu çağırırsam us_alma_islemi=sonuc gibi davranıp veri girişi yapıldığında sonuç değerini verecektir.
#ardından print ile ekrana yazdırarak terminalimde çıktısını görebilirim.

#print(us_alma_islemi(2,3))
# ya da
#deger= us_alma_islemi(2,3)
#print(deger)

#fonksiyonu bir değişkene atayarak değişken vasıtasıyla yazdırabiliriz.

#return için string değer de döndürebiliriz.Örneğin kenarları girilen üçgenin dik olup olmadığını veren fonksiyon

def hipotenus(a,b,c):
    if a**2+b**2==c**2:
        return "Dik üçgendir."
    else:
        return "Dik üçgen değildir."
    
print(hipotenus(3,4,5))

# çıktı stringdir.

