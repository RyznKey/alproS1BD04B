from mtk import *

phi = 3
print (phi)

bil_1 = int(input("masukkan bilangan 1: "))
bil_2 = int(input("masukkan bilangan 2: "))

print ("Hasil Tambah", tambah(bil_1, bil_2))
print ("Hasil Bagi", bagi(bil_1, bil_2))

"""
penjelasan;

form mtk import *: mengimpor semua fungsi dari file mtk.py

phi -= 3: mengurangi nilai phi dari file mtk.py dengan 3
print(phi): mencetak nilai phi dari file mtk.py setelah dikurangi 3

phi = 3
yang di panggil adalah variabel yang terbaru
jadi data phi yang lama tidak di panggil



bil_1: menyimpan input dari pengguna untuk bilangan 1, dikonversi menjadi integer
bil_2: menyimpan input dari pengguna untuk bilangan 2, dikonversi menjadi integer

print("Hasil Tambah", tambah(bil_1, bil_2)): mencetak hasil dari fungsi tambah dari file mtk.py dengan parameter bil_1 dan bil_2
print("Hasil Bagi", bagi(bil_1, bil_2)): mencetak hasil dari fungsi bagi dari file mtk.py dengan parameter bil_1 dan bil_2

simulasi input:
# masukkan bilangan 1: 5
# masukkan bilangan 2: 2
# fungsi tambah(5, 2): 5 + 2 = 7
# Hasil Tambah 7
# fungsi bagi(5, 2): 5 / 2 = 2.5
# Hasil Bagi 2.5
"""

