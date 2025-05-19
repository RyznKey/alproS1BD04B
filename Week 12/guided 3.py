import csv

# Data untuk ditulis ke CSV
data = [
  ['Nama', 'Umur', 'Jurusan'],
  ['Budi', 20, 'Bisnis Digital'],
  ['Ani', 21, 'Sistem Informasi'],
  ['Cahya', 19, 'Akuntansi']
]

# Menulis data ke file CSV
with open('mahasiswa.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(data)

print("Data telah ditulis ke file CSV!")

# Membaca file CSV
print("Data dari mahasiswa.csv:")
with open('mahasiswa.csv', 'r') as file:
  reader = csv.reader(file)
  for row in reader:
    print(row)

# Membaca dengan DictReader
with open('mahasiswa.csv', 'r') as file:
  # Skip header terlebih dahulu
  next(file)
  reader = csv.DictReader(file, fieldnames=['Nama', 'Umur', 'Jurusan'])
  print("\nMembaca dengan DictReader:")
  for row in reader:
    print(f"Nama: {row['Nama']}, Jurusan: {row['Jurusan']}")