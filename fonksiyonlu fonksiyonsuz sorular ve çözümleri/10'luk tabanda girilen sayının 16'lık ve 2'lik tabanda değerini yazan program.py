#10'luk tabanda girilen sayının 16'lık ve 2'lik tabanda değerini yazan program

#Onluk tabandan istenilen tabana çevirme yaparken sayıyı(onluk tabandaki) istenilen sayi değerine sonuç 1 olana kadar böleriz. Sonra en sağdan sola yazıp bitiririz
#biz işlemi pc ye yaptırdığımızda soldan sağa yazdırmış oluruz bu yüzden ters çevirmemiz gerekir. [::-1] kullanmak istediğim için sayıları str ye çevirdim
#çünkü [::-1] komutu sadece dizi,liste ve str veri tiplerinde kullanılabilir. 

def ikilik_tabana_cevirme(x):
    ikilik=""
    while x>=1:  #sonuç 1 olana kadar devam et
        kalan=x%2 # kalan bizim için anlamlı birimleri ifade ediyor
        x=x//2  
        y=str(kalan)  #tersini alabilmek için int i str ye çevirdik
        ikilik+= y  
        ters= ikilik[::-1] # tersini çevirdik
    print("İkilik taban:",ters, end="")
        
        
# 2 likteki algoritmanın aynısı sadece harfler işin içine girince 10 dan 15 e kadar olan değerleri harfe eşitlediğimizden tekrar str çevirimi yapmadık
def onaltilik_tabana_cevirme(x):
    onaltilik=""
    while x>=1:
        kalan=x%16
        x=x//16
        if kalan>9:
            if kalan==10:
                kalan="A"
            elif kalan==11:
                kalan="B"
            elif kalan==12:
                kalan="C"
            elif kalan==13:
                kalan="D"
            elif kalan==14:
                kalan="E"
            elif kalan==15:
                kalan="F"
            onaltilik+=kalan
        else:
            y=str(kalan)  #10 dan önceki ifadelerin harf karşılığı olmadığı için str ye çevirmek zorundayız
            onaltilik+=y 
        ters_cevir=onaltilik[::-1] #ters çevirdik
    print("On altılık taban:",ters_cevir, end="")
            


#fonksiyonlarımızın içinde print komutlerı olduğu için yazdırmak için sadece fonksiyonu çağırmamız yeterli olacak 
sayi=int(input("Sayi girişi yapınız: "))
print()
ikilik_tabana_cevirme(sayi)
print() # yan yana yazdırmasın diye kullandık print()'de default değeri \n ifadesi vardır.
onaltilik_tabana_cevirme(sayi)


#seninle grur duyuyorum bebişim muah <3