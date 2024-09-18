#Girilen metinin tersini yazdıran program

#[::-1] ifadesi her zaman tersten yazdırmak için kullanılır. Kullanım şekli ise istediğimiz veriyi alıp [::-1] ifadesini yanına ekleyerek baska bir değişkene atamak.
#ardından bu yeni değişkeni yazdırarak tersten yazdırabilirsin.  

#bu method yani [::-1], sadece dilimlenebilir (slicable) veri tiplerinde kullanılabilir. Bunlar str, liste ve dizilerdir. Sayılar için bu methodu kullanamayız.
#fakat bunun da bir bugı var :) int i önce str ye çevirip işlemi yaptırıp sonra tekrar int e çevirebilirz. ör: 
# x=1321315 (input olarak alınabilir)    y= int(str(y)[::-1])


def terstenYazdirma(x):
    y=x[::-1]
    return y
  
metin=(input("Metin giriniz: "))  #metin örneği
print(terstenYazdirma(metin))


liste=list(input("Liste oluştur")) #liste örneği
print(terstenYazdirma(liste))