class Hewan:
  def __init__(self, nama):
    self.nama = nama

  def suara(self):
    print("Tidak diketahui")

class Kucing(Hewan):
  def suara(self):
    print(f"{self.nama} mengeluarkan suara: Meong!")

class Anjing(Hewan):
  def suara(self):
    print(f"{self.nama} mengeluarkan suara: Guk Guk!")

# Membuat objek dari kelas berbeda
kucing = Kucing("Kitty")
anjing = Anjing("Doggy")

# Memanggil method yang sama pada objek berbeda
kucing.suara()  # Output: Kitty mengeluarkan suara: Meong!
anjing.suara()  # Output: Doggy mengeluarkan suara: Guk Guk!

# Daftar hewan
daftar_hewan = [Kucing("Milo"), Anjing("Rex"), Kucing("Luna")]

# Memanggil method suara() untuk semua hewan
for hewan in daftar_hewan:
  hewan.suara()