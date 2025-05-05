class Mahasiswa:
  # Constructor
  def __init__(self, nama, nim):
    self.nama = nama  # Public attribute
    self.nim = nim    # Public attribute

  # Method
  def tampilkan_info(self):
    print(f"Nama: {self.nama}, NIM: {self.nim}")


# Membuat objek dari kelas Mahasiswa
mhs1 = Mahasiswa("Falah Akbar", "22001")
mhs2 = Mahasiswa("Iqbal Rasyid", "22002")

# Memanggil method dari objek
mhs1.tampilkan_info()
mhs2.tampilkan_info()

# Mengakses atribut objek
print(f"Nama mahasiswa 1: {mhs1.nama}")
print(f"NIM mahasiswa 2: {mhs2.nim}")