# tebak_umur.py

# Input usia dari pengguna
usia = int(input("Masukkan usia: "))

# Menentukan kategori berdasarkan usia
if usia <= 5:
  print("Dia adalah balita.")
elif usia > 5 and usia <= 12:
  print("Dia adalah anak-anak.")
elif usia > 12 and usia < 18:
  print("Dia adalah remaja.")
else:
  print("Dia adalah dewasa.")