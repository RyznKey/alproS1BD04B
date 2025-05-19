import os
# 
# Mendapatkan direktori kerja saat ini
current_dir = os.getcwd() # mengambail path dir kerja saat ini.
print(f"Direktori kerja saat ini: {current_dir}")

# Cek apakah sebuah file ada
file_exists = os.path.exists("contoh.txt") # mengevek pakah file contoh.txt ada
print(f"Apakah file contoh.txt ada? {file_exists}")

# Membuat direktori baru
dir_name = "data_files_pathDirectory"
try:
  os.mkdir(dir_name) # membuat dir baru benama data_file_pathDirectory. jika
  print(f"Direktori {dir_name} berhasil dibuat!")
except FileExistsError:
  print(f"Direktori {dir_name} sudah ada!")

# Membuat file dalam direktori baru
#  mengambungkan file menjadi satu
file_path = os.path.join(dir_name, "test.txt") # membuat file baru benama text.txt di ....
with open(file_path, "w") as file: 
  file.write("Ini adalah file dalam direktori baru.\n")

print(f"File berhasil dibuat di {file_path}")