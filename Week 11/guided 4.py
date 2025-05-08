from abc import ABC, abstractmethod

# Latihan 4 - Abstraction

class BentukAbstrak(ABC):
  @abstractmethod
  def hitung_luas(self):
    pass

class Persegi(BentukAbstrak):
  def __init__(self, sisi):
    self.sisi = sisi

  def hitung_luas(self):
    return self.sisi * self.sisi

class Lingkaran(BentukAbstrak):
  def __init__(self, jari):
    self.jari = jari

  def hitung_luas(self):
    return 3.14 * self.jari * self.jari

# Penggunaan
try:
  bentuk = BentukAbstrak()  # Error: kelas abstrak
except TypeError as e:
  print("Tidak bisa membuat objek dari kelas abstrak")

persegi = Persegi(5)
lingkaran = Lingkaran(7)

print(f"Luas persegi: {persegi.hitung_luas()}")  # 25
print(f"Luas lingkaran: {lingkaran.hitung_luas()}")  # 153.86