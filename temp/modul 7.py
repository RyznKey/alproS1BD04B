"""
TUGAS MODUL 7
NAMA  : AHSAN MAULANA RIZQI
NIM   : 104062400071
KELAS : S1 BD 04 B
DOSEN : ERLINA NUR ARIFANI S.T.P, M.Sc.
"""

"""
SOAL 
1. Membuat program Untuk Menampilkan Bilangan Kelipatan 3 Dari 1 Hingga 100.
2. Membuat program untuk menghitung faktorial dari sebuah angka.
3. Membuat program untuk menampilkan pola segitiga terbalik dengan tinggi yang ditentukan oleh user.
"""

# # Soal nomor 1
# # variabel untuk soal nomor 1
# limit = 100     # batas kelipatan 3
# jumlah = 0      # inisialisasi jumlah

# # vesi 1
# print("\nCode Versi 1 Soal Nomor 1")
# kelipatan = []  # inisialisasi list kelipatan 3 
# while True:                      # loop untuk mencari kelipatan 3
#   if jumlah % 3 == 0:            # jika jumlah habis dibagi 3
#     kelipatan.append(jumlah)     # menambahkan jumlah ke list jika habis dibagi 3
#   if jumlah == limit:            # jika jumlah sudah mencapai batas
#     break
#   jumlah += 1
# print("kelipatan 3 dari 0 sampai 100 adalah: ", kelipatan, "\n")  # menampilkan list kelipatan 3

# # versi 2.1
# print("\nCode Versi 2.1 Soal Nomor 1")
# kelipatan = []                  # inisialisasi list kelipatan 3
# for i in range(0, limit + 1):   # loop untuk mencari kelipatan 3
#   if i % 3 == 0:                # jika i habis dibagi 3
#     kelipatan.append(i)         # menambahkan i ke list jika habis dibagi 3
# print("kelipatan 3 dari 0 sampai 100 adalah: ", kelipatan, "\n")  # menampilkan list kelipatan 3

# # versi 2.2
# print("\nCode Versi 2.2 Soal Nomor 1")
# kelipatan = [i for i in range(0, limit + 1) if i % 3 == 0]        # list comprehension untuk mencari kelipatan 3 
# print("kelipatan 3 dari 0 sampai 100 adalah: ", kelipatan, "\n")  # menampilkan list kelipatan 3

# Note soal nomor 1
"""
  kelipatan adalah bilangan yang dapat dibagi oleh bilangan lain tanpa sisa.
  contoh: kelipatan 3 adalah 0, 3, 6, 9, 12, ..., 99.

  list comprehension adalah cara singkat untuk membuat list baru dari list yang sudah ada dengan kondisi tertentu.
  contoh: kelipatan = [i for i in range(0, limit + 1) if i % 3 == 0] 

  method append() digunakan untuk menambahkan elemen ke dalam list.
  contoh: kelipatan.append(jumlah) yang artinya hasil dari variabel jumlah dimasukan ke dalam list kelipatan.

  FAQ:
  - kenapa menggunakan list comprehension?
    karena lebih singkat dan lebih mudah dibaca.
  - Di bagian mana jika saya ingin mengganti batas yang harus diubah?
    cukup ganti variabel limit pada kode di atas.
"""

# # Soal nomor 2
# # variabel untuk soal nomor 2
# nilai = 3 # input nilai untuk faktorial

# # Versi 1
# print("\nCode Versi 1 Soal Nomor 2")
# for i in reversed(range(1, nilai + 1)):          # loop untuk mencari faktorial
#   hasil = nilai * (nilai - 1)                    # menghitung faktorial
# print(f"faktorial dari {nilai} adalah {hasil}")  # menampilkan hasil faktorial

# # Versi 2
# print("\nCode Versi 2 Soal Nomor 2")
# def faktorial(nilai):             # mendefinisikan fungsi faktorial
#   if nilai == 0 or nilai == 1:    # jika nilai 0 atau 1 agar tidak terjadi rekursi tak terhingga
#     return 1                      # mengembalikan 1 jika nilai 0 atau 1
#   else:
#     return nilai * faktorial(nilai - 1)                     # rekursi untuk menghitung faktorial
# print(f"faktorial dari {nilai} adalah {faktorial(nilai)}")  # menampilkan hasil faktorial

# note soal nomor 2
"""
  faktorial adalah hasil kali dari semua bilangan bulat positif dari 1 sampai n.
  contoh: faktorial dari 5 adalah 5 * 4 * 3 * 2 * 1 = 120
  faktorial dari 0 adalah 1.
  faktorial dari 1 adalah 1.

  fungsi rekursif adalah fungsi yang memanggil dirinya sendiri.
  contoh: fungsi faktorial di atas memanggil dirinya sendiri dengan nilai yang lebih kecil sampai mencapai 0 atau 1.

  konsep faktorial adalah sebagai berikut:
  - faktorial dari n adalah n * (n-1)!
  - faktorial dari 0 adalah 1.
  - faktorial dari 1 adalah 1.

  jika ingin mengganti nilai faktorial, cukup ganti nilai variabel 'nilai' pada kode di atas.
"""

# Soal nomor 3
# variabel untuk soal nomor 3
sisi = int (input("\nmasukan sisi segitiga: ")) # input sisi segitiga
spasi = 0                                       # jumlah spasi

# Versi 1
print("\nCode Versi 1 Soal Nomor 3")
count = sisi  # jumlah bintang
while True:   # loop untuk mencetak segitiga

  if count % 2: # jika jumlah bintang ganjil
    print(" " * spasi , "*" * count) # mencetak spasi dan bintang
    count -= 1  # mengurangi jumlah bintang
    spasi += 1  # menambah jumlah spasi
  else:         # jika jumlah bintang genap
    count -= 1  # mengurangi jumlah bintang
    continue    # lanjut ke iterasi berikutnya

  if count == 0:
    break       # keluar dari loop

# Versi 2
print("\n Code Versi 2 Soal Nomor 3")
# Loop untuk pola segitiga
for count in reversed(range(1, sisi, 2)):  # Menggunakan step 2 untuk pola segitiga
    print(" " * spasi + "*" * count)       # Mencetak spasi dan bintang
    spasi += 1                             # Mengurangi spasi setiap kali ke baris berikutnya

# Note soal nomor 3
"""
  pola segitiga adalah pola yang dibentuk oleh bintang (*) dan spasi.
  contoh: pola segitiga dengan sisi 5 adalah:
    *
   ***
  *******
  
  fungsi reversed() digunakan untuk membalik urutan elemen dalam range.
  fungsi range() digunakan untuk menghasilkan urutan angka dari 1 sampai sisi dengan step 2.
"""