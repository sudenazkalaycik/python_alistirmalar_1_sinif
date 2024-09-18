#boyutu girilen iki random matris oluşturup toplamını bulan program
import random

def write_matrix(matrix,name):  #matris yazdıran kısım
     print(name)
     for i in range(len(matrix)):
          for j in range(len(matrix[i])):
               print(matrix[i][j],end=" ")
          print()
     

d=3

matrix_1=[[int(10*random.random())for i in range(d)]for j in range(d)]
matrix_2=[[int(10*random.random())for i in range(d)]for j in range(d)]
result_matrix=[[0 for i in range(d)] for j in range(d)]

for i in range(d):
     for j in range(d):
          result_matrix[i][j]=matrix_1[i][j]+matrix_2[i][j]

write_matrix(result_matrix, name="Matris")


"""# matris oluşturma random ile 
import random
Matris=[]
n=5
m=10

#bu kod satırını tek satırda yukarıda olduğu gibi yazdırabiliyoruz
for i in range(n):
    liste=[]
    for j in range(m):
        liste.append(random.randint(1,9))
    Matris.append(liste)   


for i in range(len(Matris)):
    for j in range(len(Matris[0])):
        print(Matris[i][j], end=" ")
    print()
    
    
"""