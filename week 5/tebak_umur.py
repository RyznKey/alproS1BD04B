# code program tebak umur
# Program untuk menebak umur seseorang berdasarkan input usia

# Input usia dari pengguna
usia = int(input("Masukkan usia: "))

# Menentukan kategori berdasarkan usia
if usia <= 5: # statement pertama untuk memeriksa usia, jika usia kurang dari atau sama dengan 5
  print("Dia adalah balita.") # mencetak "Dia adalah balita"
elif usia > 5 and usia <= 12: # statement kedua untuk memeriksa usia, jika usia lebih dari 5 dan kurang dari atau sama dengan 12
  print("Dia adalah anak-anak.") # mencetak "Dia adalah anak-anak"
elif usia > 12 and usia < 18: # statement ketiga untuk memeriksa usia, jika usia lebih dari 12 dan kurang dari 18
  print("Dia adalah remaja.") # mencetak "Dia adalah remaja"
else: # statement tidak ada yang memenuhi kondisi sebelumnya, statement ini akan dijalankan
  print("Dia adalah dewasa.") # mencetak "Dia adalah dewasa"