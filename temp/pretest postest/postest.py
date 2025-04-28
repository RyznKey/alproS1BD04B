import math

# Program untuk membaca angka bulan dan mencetak nama bulan

# Daftar nama bulan yang disimpan pada array 
nama_bulan = [
  "Januari", "Februari", "Maret", "April", "Mei", "Juni",
  "Juli", "Agustus", "September", "Oktober", "November", "Desember"
]

# Membaca input angka bulan
angka_bulan = int(input("Masukkan angka bulan (1-12): "))

# Memeriksa validitas angka bulan dan mencetak nama bulan
# jika angka bulan antara 1 dan 12, maka mencetak nama bulan
if 1 <= angka_bulan <= 12:
  print(f"Bulan ke-{angka_bulan} adalah {nama_bulan[angka_bulan - 1]}")
# jika angka bulan tidak valid, maka mencetak pesan error
else:
  print("Angka bulan tidak valid. Masukkan angka antara 1 dan 12.")

  
# Program untuk menampilkan menu dan membaca pilihan
# variabel
menu_nama = ["Baca Data", "Cetak Data", "Ubah Data", "Hapus Data"]

while True:
  # Menampilkan pesan menu
  display = f"""
======== MENU ========
1. {menu_nama[0]}
2. {menu_nama[1]}
3. {menu_nama[2]}
4. {menu_nama[3]}
======================
"""
  print (display)

  # input pilihan menu
  pilihan = int(input("Masukkan Pilihan Anda: "))
  print ("========================")

  # menampilkan pesan sesuai pilihan
  if 1 <= pilihan <= 4:
    print(f"Anda memilih menu nomor {pilihan}, yaitu {menu_nama[pilihan - 1]}")
  else:
    print("Pilihan tidak valid. Masukkan angka antara 1 dan 4.")


