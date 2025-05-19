# membuat file contoh.txt

# Menulis ke file teks
# mengunakan alias "as" sebagai file
with open("contoh.txt", "w") as file: # membuat file contoh.txt  lalu menulis dua baris 
  file.write("Ini adalah baris pertama.\n") # menulis baris baru
  file.write("Ini adalah baris kedua.\n")

print("File telah ditulis!")

# Membaca dari file teks
with open("contoh.txt", "r") as file: # membuka file dan membaca semua isinya lalu mencetaknya
  content = file.read() # sebuah variabel untk memanggil file.read() / membaca file contoh.txt
  print("Isi file:") 
  print(content)

# Menambahkan konten ke file
with open("contoh.txt", "a") as file: # mrmuka file dalam mode append lalu menambhakannya
  file.write("Ini adalah baris yang ditambahkan.\n") 

print("Konten telah ditambahkan!")

# Membaca file baris per baris
with open("contoh.txt", "r") as file:
  print("Membaca baris per baris:")
  # mencetak setiap variabel
  for line in file: # membaca isi file baris demi baris 
    print(line.strip())  # strip() menghilangkan karakter newline