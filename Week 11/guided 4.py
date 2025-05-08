from abc import ABC, abstractmethod # Abstract Base Class

# Latihan 4 - Abstraction = pewarisn degan method yang sama pada class yang berbeda
# Abstraksi adalah proses menyembunyikan detail implementasi dan hanya menampilkan fitur penting dari objek

class BentukAbstrak(ABC): # Kelas abstrak
  @abstractmethod # moderator untuk membuat class abstrak
  def hitung_luas(self): # Method abstrak
    pass # Tadak ada implementasi di kelas abstrak tapi tetap berjalan

class Persegi(BentukAbstrak):
  def __init__(self, sisi):
    self.sisi = sisi

  def hitung_luas(self):
    return self.sisi * self.sisi

class Lingkaran(BentukAbstrak): # Kelas Lingkaran mewarisi kelas BentukAbstrak
  def __init__(self, jari): # Constructor
    self.jari = jari # Inisialisasi atribut jari-jari

  def hitung_luas(self): # Implementasi method abstrak
    return 3.14 * self.jari * self.jari # Menghitung luas lingkaran dengan rumus πr²
  
class Segitiga(BentukAbstrak): # Kelas Segitiga mewarisi kelas BentukAbstrak
  def __init__(self, alas, tinggi): # Constructor
    self.alas = alas # Inisialisasi atribut alas
    self.tinggi = tinggi # Inisialisasi atribut tinggi

  def hitung_luas(self): # Implementasi method abstrak
    return 0.5 * self.alas * self.tinggi # Menghitung luas segitiga dengan rumus 1/2 * alas * tinggi

# Penggunaan
try:
  bentuk = BentukAbstrak()  # Error: kelas abstrak
except TypeError as e:
  print("Tidak bisa membuat objek dari kelas abstrak")

persegi = Persegi(5) # Membuat objek persegi dengan argumentasinya 5
lingkaran = Lingkaran(7)  # Membuat objek lingkaran dengan jari-argunemtasinya 7
segitiga = Segitiga(4, 6) # Membuat objek segitiga dengan alas 4 dan tinggi 6

print(f"Luas persegi: {persegi.hitung_luas()}")  # 25
print(f"Luas lingkaran: {lingkaran.hitung_luas()}")  # 153.86
print(f"Luas segitiga: {segitiga.hitung_luas()}")  # 12.0