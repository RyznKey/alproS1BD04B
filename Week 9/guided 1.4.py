x = lambda a: a + 10
print(x(5))

x = lambda a,b : a % b
print (x(5, 3))

x = lambda a,b,c : a+b-c
print (x(5,3,2))

"""
fungsi def adalah fungsi yang memiliki nama dan dapat memiliki banyak baris kode
fungsi lambda adalah fungsi yang tidak memiliki nama dan hanya dapat memiliki satu baris kode

fungsi lambda fungsi sementara
fungsi def butuh pemmggilan untuk 

variabel x menyimpan fungsi lambda dengan parameter a dan mengembalikan nilai a + 10
print(x(5)): mencetak hasil dari fungsi lambda dengan parameter 5
5 + 10 = 15
hasilnya adalah 15

variabel x menyimpan fungsi lambda dengan parameter a dan b dan mengembalikan nilai a % b
print(x(5, 3)): mencetak hasil dari fungsi lambda dengan parameter 5 dan 3 
5 % 3 = 2
hasilnya adalah 2

varibel x menyimpan fungsi lambda dengan parameter a, b, dan c dan mengembalikan nilai a + b - c
print(x(5,3,2)): mencetak hasil dari fungsi lambda dengan parameter 5, 3, dan 2
5 + 3 - 2 = 6
hasilnya adalah 6
"""