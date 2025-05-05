class Kategori:
  def __init__(self, nama):
    self.nama = nama

class Produk:
  def __init__(self, kode, nama, harga, kategori):
    self.kode = kode
    self.nama = nama
    self.harga = harga
    self.kategori = kategori

  def info(self):
    print(f"Kode: {self.kode}")
    print(f"Nama: {self.nama}")
    print(f"Harga: Rp{self.harga}")
    print(f"Kategori: {self.kategori.nama}")

# Contoh penggunaan
if __name__ == "__main__":
  # Membuat kategori
  kat_elektronik = Kategori("Elektronik")
  kat_pakaian = Kategori("Pakaian")

  # Membuat produk
  laptop = Produk("P001", "Laptop Gaming", 8000000, kat_elektronik)
  kaos = Produk("P002", "Kaos Skena", 150000, kat_pakaian)

  # Menampilkan informasi produk
  print("=== Info Produk 1 ===")
  laptop.info()
  print("\n=== Info Produk 2 ===")
  kaos.info()