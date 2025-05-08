class Mahasiswa:
  # Constructor
  def __init__(self, nama, nim): # init variabel yang digunakan untuk menentukan konteks
    self.nama = nama  # Public attribute 
    self.nim = nim    # Public attribute
    
  # Method
  def tampilkan_info(self): # mengambil parameter method dari self class utama
    print(f"Nama: {self.nama}, NIM: {self.nim}") 


# Membuat objek dari kelas Mahasiswa
mhs1 = Mahasiswa("Falah Akbar", "22001") # object yg berisi nama dan nim
mhs2 = Mahasiswa("Iqbal Rasyid", "22002")

# Memanggil method dari objek
mhs1.tampilkan_info() 
# memenggil method dari objek mhs1 untuk ditampilkan 
mhs2.tampilkan_info()

# Mengakses atribut objek
print(f"Nama mahasiswa 1: {mhs1.nama}") #mengs
# untuk memanggil nama mahasiswa 1 nama nya saja
print(f"NIM mahasiswa 2: {mhs2.nim}")
# untuk memanggil nim mahasiswa 2

"""
nama claas utama yaitu Mahasiswa
memiliki constructor __init__ yang berfungsi untuk menginisialisasi atribut nama dan nim
memiliki method tampilkan_info yang berfungsi untuk menampilkan informasi mahasiswa
method tampilkan_info menggunakan f-string untuk format string

f digunakan untuk mengubah tipe data ke f-string
"""