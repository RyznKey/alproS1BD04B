phi = 3.14159
nama = "Budi"

def hello():
  print ("Hello Nama saya ", nama, "!")

def tambah(angka1, angka2):
  hasil = angka1 + angka2
  return hasil

def bagi (angka1, angka2):
  if angka2 != 0:
    hasil = angka1 / angka2
    return hasil
  else:
    return "error: Pembagian dengan nol"
  

# print(hello())
# print(tambah(5, 10))
# print(bagi(10, 2))

"""
penjelasan:

variabel phi: menyimpan nilai 3.14159
variabel nama: menyimpan string "Budi"

fungsi hello: menerima parameter nama dan mencetak "Hello Nama saya !"
fungsi tambah: menerima dua parameter angka1 dan angka2, menjumlahkan keduanya, dan mengembalikan hasilnya
hasil = angka1 + angka2
mengembalikan nilai hasil
fungsi bagi: menerima dua parameter angka1 dan angka2,jika angka2 tidak sama dengan 0, maka membagi angka1 dengan angka2, dan mengembalikan hasilnya. Jika angka2 nol, mengembalikan pesan error

"""