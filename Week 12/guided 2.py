import os

# Mendapatkan direktori kerja saat ini
current_dir = os.getcwd()
print(f"Direktori kerja saat ini: {current_dir}")

# Cek apakah sebuah file ada
file_exists = os.path.exists("contoh.txt")
print(f"Apakah file contoh.txt ada? {file_exists}")

# Membuat direktori baru
dir_name = "data_files_pathDirectory"
try:
  os.mkdir(dir_name)
  print(f"Direktori {dir_name} berhasil dibuat!")
except FileExistsError:
  print(f"Direktori {dir_name} sudah ada!")

# Membuat file dalam direktori baru
file_path = os.path.join(dir_name, "test.txt")
with open(file_path, "w") as file:
  file.write("Ini adalah file dalam direktori baru.\n")

print(f"File berhasil dibuat di {file_path}")