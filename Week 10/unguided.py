# Kelas dasar
class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk 
        self.tahun = tahun

    def tampilkan_info(self):
        print(f"Merk: {self.merk}")
        print(f"Tahun: {self.tahun}")

# Kelas turunan
class Mobil(Kendaraan):
    def _init_(self, merk, tahun, tipe):
        super()._init_(merk, tahun)
        self.tipe = tipe

    def tampilkan_info(self):
        # Override method dari kelas Kendaraan
        print(f"Merk: {self.merk}")
        print(f"Tahun: {self.tahun}")
        print(f"Tipe: {self.tipe}")

# Membuat objek dari kelas Mobil
mobil_saya = Mobil("Toyota", 2022, "SUV")
mobil_saya.tampilkan_info()