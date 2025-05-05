# Kelas dasar (parent class)
class Pengguna:
  def __init__(self, nama, email):
    self.nama = nama
    self.email = email

  def tampilkan_info(self):
    print(f"Nama: {self.nama}")
    print(f"Email: {self.email}")

# Kelas turunan (child class)
class MahasiswaDigital(Pengguna):
  def __init__(self, nama, email, nim, jurusan):
    # Memanggil constructor parent class
    super().__init__(nama, email)
    self.nim = nim
    self.jurusan = jurusan

  # Override method dari parent class
  def tampilkan_info(self):
    super().tampilkan_info()  # Memanggil method parent
    print(f"NIM: {self.nim}")
    print(f"Jurusan: {self.jurusan}")

# Membuat objek dari kelas turunan
mhs_digital = MahasiswaDigital("Aloy Renaloy", "aloy@gmail.com", "BD003", "Bisnis Digital")
mhs_digital.tampilkan_info()