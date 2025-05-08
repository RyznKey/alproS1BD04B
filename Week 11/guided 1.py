# Latihan 1 - Inheritance 3 tingkat: Hewan -> Kucing -> Anggora
class Hewan: # parent class
  def __init__(self, nama):
    self.nama = nama

  def suara(self):
    return "Suara hewan"

class Kucing(Hewan): # membuat class Kucing yang merupakan turunan dari class Hewan
  def suara(self): # mengamilkan method suara dari class Hewan
    return "Meong"

class Anggora(Kucing): # membuat class Anggora yang merupakan turunan dari class Kucing
  def __init__(self, nama, warna,tahun): # mengambil parameter dari class Kucing
    super().__init__(nama) 
    self.warna = warna
    self.tahun = tahun

  def deskripsi(self): 
    return f"{self.nama} adalah kucing anggora {self.warna} berusia {self.tahun} tahun"

# Penggunaan
hewan = Hewan("Binatang")
kucing = Kucing("Tom")
anggora = Anggora("Kitty", "putih", "3")

print(hewan.suara())       # Suara hewan
print(kucing.suara())      # Meong
print(anggora.suara())     # Meong
print(anggora.deskripsi()) # Kitty adalah kucing anggora putih berusia 3 tahun