# Definisi kelas Hewan sebagai kelas induk
class Hewan:
  def __init__(self, nama):
    self.nama = nama  # Inisialisasi atribut nama

  def suara(self):
    # Method suara() default untuk kelas Hewan
    print("Tidak diketahui")

# Definisi kelas Kucing yang mewarisi kelas Hewan
class Kucing(Hewan):
  def suara(self):
    # override dari 
    # Override method suara() untuk kelas Kucing
    print(f"{self.nama} mengeluarkan suara: Meong!")

# Definisi kelas Anjing yang mewarisi kelas Hewan
class Anjing(Hewan):
  def suara(self):
    # Override method suara() untuk kelas Anjing
    print(f"{self.nama} mengeluarkan suara: Guk Guk!")

# Membuat objek dari kelas Kucing dan Anjing
kucing = Kucing("Kitty")  # Objek kucing dengan nama "Kitty"
anjing = Anjing("Doggy")  # Objek anjing dengan nama "Doggy"

# Memanggil method suara() pada objek kucing dan anjing
kucing.suara()  # Output: Kitty mengeluarkan suara: Meong!
anjing.suara()  # Output: Doggy mengeluarkan suara: Guk Guk!

# Membuat daftar hewan yang berisi objek Kucing dan Anjing
daftar_hewan = [Kucing("Milo"), Anjing("Rex"), Kucing("Luna")]

# Menggunakan perulangan untuk memanggil method suara() pada setiap objek dalam daftar
for hewan in daftar_hewan:
  hewan.suara()  # Output sesuai dengan jenis hewan