# Kelas dasar (Base class)
class Kendaraan():
    def __init__(self, merk, tahun):
        # Inisialisasi atribut merk dan tahun
        self.merk = merk 
        self.tahun = tahun

    def tampilkan_info(self):
        # Method untuk menampilkan informasi kendaraan
        print(f"Merk: {self.merk}")
        print(f"Tahun: {self.tahun}")

# Kelas turunan (Derived class)
class Mobil(Kendaraan):
    def __init__(self, merk, tahun, tipe):  
        # Memanggil konstruktor kelas dasar
        super().__init__(merk, tahun)
        # Inisialisasi atribut tambahan untuk kelas Mobil
        self.tipe = tipe

    def tampilkan_info(self):
        # Override method tampilkan_info dari kelas Kendaraan
        print(f"Merk: {self.merk}")
        print(f"Tahun: {self.tahun}")
        print(f"Tipe: {self.tipe}")

# Membuat objek dari kelas Mobil
mobil_saya = Mobil("Toyota", 2022, "SUV")
# Memanggil method tampilkan_info untuk menampilkan informasi mobil
mobil_saya.tampilkan_info()