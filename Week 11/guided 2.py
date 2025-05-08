# Latihan 2 - Encapsulation
class Siswa:
  def __init__(self, nama, nilai):
    self.nama = nama              # Public
    self._kelas = "10A"           # Protected
    self.__nilai = nilai          # Private

  def get_nilai(self):
    return self.__nilai

  def set_nilai(self, nilai_baru):
    if 0 <= nilai_baru <= 100:
      self.__nilai = nilai_baru
      return True
    return False

# Penggunaan
siswa = Siswa("Andi", 85)

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