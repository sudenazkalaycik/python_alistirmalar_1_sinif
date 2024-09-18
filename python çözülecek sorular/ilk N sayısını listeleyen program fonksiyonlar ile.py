#İlk N sayısını listleyen program

a=int(input("Sayı giriniz:"))
def n_sayi(a):
    liste=[]
    for i in range(a):
        liste.append(i)
    return liste

print(n_sayi(a))  
