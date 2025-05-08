# Latihan 2 - Encapsulation
class Siswa:
  #constructor
  def __init__(self, nama, nilai):
    self.nama = nama              # Public
    self._kelas = "10A"           # Protected attribute protected = ga bisa diakses diluar class tapi bisa diakses di subclass
    self.__nilai = nilai          # Private attribute private = ga bisa diakses diluar class hanya bisa diakses di class itu sendiri

  def get_nilai(self): # Getter nilai
    return self.__nilai

  def set_nilai(self, nilai_baru): # Setter nilai
    if 0 <= nilai_baru <= 100: 
      self.__nilai = nilai_baru
      return True
    return False

# Penggunaan
siswa = Siswa("Andi", 85) # Membuat objek variable siswa

# Akses atribut
print(siswa.nama)          # Andi (public)
print(siswa._kelas)        # 10A (protected)

# Akses private attribute
try:
  print(siswa.__nilai)   # Error
except AttributeError:
  print("Tidak bisa akses langsung nilai private")

# Getter dan setter
print(siswa.get_nilai())   # 85
siswa.set_nilai(90)
print(siswa.get_nilai())   # 90