#Girilen sayının kaç faktöriyel olduğunu bulunuz 

sayi=int(input("Sayı giriniz:"))
def faktoriyel_bul(sayi):
    bolen=1
    while sayi%bolen==0:
        if sayi>=1:
            sayi/=bolen
            bolen+=1
            if sayi==1:
                bolen-=1
                print(f"Bu sayının faktöriyeli {bolen}!")  
                quit()

    print("Bu sayının faktröriyeli yoktur") 



faktoriyel_bul(sayi)