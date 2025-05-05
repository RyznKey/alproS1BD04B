class MahasiswaBisnis:
  def __init__(self, nama, nim):
    self.nama = nama          # Public attribute
    self.__nim = nim          # Private attribute (diawali dengan __)

  # Method untuk mendapatkan NIM
  def get_nim(self):
    return self.__nim

  # Method untuk mengubah NIM
  def set_nim(self, nim_baru):
    self.__nim = nim_baru

  def tampilkan_info(self):
    print(f"Nama: {self.nama}, NIM: {self.__nim}")


# Membuat objek
mhs = MahasiswaBisnis("Vincent", "BD001")
mhs.tampilkan_info()

# Mengakses private attribute melalui getter
print(f"NIM: {mhs.get_nim()}")

# Mengubah nilai private attribute melalui setter
mhs.set_nim("BD002")
mhs.tampilkan_info()