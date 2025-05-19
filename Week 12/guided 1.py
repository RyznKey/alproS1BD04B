# Menulis ke file teks
with open("contoh.txt", "w") as file:
  file.write("Ini adalah baris pertama.\n")
  file.write("Ini adalah baris kedua.\n")

print("File telah ditulis!")

# Membaca dari file teks
with open("contoh.txt", "r") as file:
  content = file.read()
  print("Isi file:")
  print(content)

# Menambahkan konten ke file
with open("contoh.txt", "a") as file:
  file.write("Ini adalah baris yang ditambahkan.\n")

print("Konten telah ditambahkan!")

# Membaca file baris per baris
with open("contoh.txt", "r") as file:
  print("Membaca baris per baris:")
  for line in file:
    print(line.strip())  # strip() menghilangkan karakter newline