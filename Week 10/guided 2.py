class MahasiswaBisnis: # Class MahasiswaBisnis adalah class utama
  #  memgnggil untuk semua parameter yang ada di dalam class
  def __init__(self, nama, nim): # self adalah parameter yang digunakan untuk mengacu pada objek itu sendiri
    self.nama = nama          # Public attribute  
    # memgambil object mengguanakan self
    self.__nim = nim          # Private attribute (diawali dengan __)

  # Method untuk mendapatkan NIM
  def get_nim(self):           # self diambil dari class utama
    return self.__nim          # Mengambil nim yang private dari class utama

  # Method untuk mengubah NIM
  def set_nim(self, nim_baru): # self diambil dari class utama 
    self.__nim = nim_baru      # Mengubah nim yang private dari class utama

  def tampilkan_info(self):
    print(f"Nama: {self.nama}, NIM: {self.__nim}")


# Membuat objek
mhs = MahasiswaBisnis("Vincent", "BD001") # object yg berisi nama dan nim 
# MahasiswaBisnis mengabil dari class diatas
mhs.tampilkan_info() # Menampilkan informasi mahasiswa

# Mengakses private attribute melalui getter
print(f"NIM: {mhs.get_nim()}")            # Mengabil nilai nim yang private dari class utama
"""
jika susdah mengambil private attribute nim, maka bisa diubah
"""
# Mengubah nilai private attribute melalui setter
mhs.set_nim("BD002") # Mengubah nim yang private dari class utama
mhs.tampilkan_info() # Menampilkan informasi mahasiswa setelah diubah

"""
private variabel hanya beberapa saja yang dapat dipakai di dalam class itu sendiri
"""