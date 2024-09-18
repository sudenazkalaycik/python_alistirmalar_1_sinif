#Girilen metindeki harflerin ASCII değerlerine bakarak eğer küçük harfle yazıldıysa büyük hale dönüştüren program
#sadece ingilizce karakterler için geçerli
def harf_buyutme(x):
    bos_metin=""
    for i in x:
        ascii=ord(i)
        if 97<=ascii<=122:
            i= chr(ascii-32)
            bos_metin+=i
        else:
            bos_metin+=i
    return bos_metin



metin=input("Metin giriniz: ")
print(harf_buyutme(metin))
            












