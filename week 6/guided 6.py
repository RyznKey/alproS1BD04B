x = 0 # Inisialisasi variabel x
while True: # Looping tanpa batas
  nama = input("Masukkan nama anda: ")  # Meminta input nama dari pengguna
  print("Nama anda adalah: ", nama) # Menampilkan nama yang dimasukkan
  x += 1  # Menambah nilai x setiap iterasi
  if x == 5: # Jika x yang dimasukkan adalah 5, keluar dari loop
    break   # break statement untuk keluar dari loop