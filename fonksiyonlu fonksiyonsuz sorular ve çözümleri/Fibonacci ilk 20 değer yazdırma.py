#Fibonacci ilk 20 değeri yazdıran program
#sayi=int(input("İlk kaç değeri yazdırmak istersiniz:"))  #(opsiyonel)
x,y=1,1
print(x,y, end=" ")
for i in range(18): #(sayi-2) opsiyonel
    sonuc=x+y  #  x (n. sayı) ve y (n+1. sayı) değerlerini toplayıp yeni (n+2.) sayıyı elde ettim.
    print(sonuc, end=" ")  #değeri yazdırdım ve aslında burada program bitiyor asıl bir sonraki adım döngüyü devam ettiren nokta.
    x=y # x => n. sayi, y =>n+1. sayı idi. Şimdi ise x n+1. sayı oldu
    y=sonuc # x, y nin değerini alınca y değersiz kaldı. Kendini kötü hissetmesin diye de ona n+2. değeri verdik.
    
    
#dönünce bakınca anlamıycan ya sudiş ondan aptala anlatır gibi anlattım bitanem :)  canım kendim
    
