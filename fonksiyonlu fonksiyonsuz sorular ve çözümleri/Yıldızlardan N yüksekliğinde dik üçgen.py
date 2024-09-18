#Yıldızlardan N yüksekliğinde dik üçgen yazdıran program
N=int(input("Üçgenin yükseklik değerini giriniz:"))
sayac=0
for i in range(N):
    if sayac<N:
        print("*"*i)