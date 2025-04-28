class Mahasiswa:
  def __init__(self, nama, nilai1, nilai2, nilai3):
    self.nama = nama
    self.nilai1 = nilai1
    self.nilai2 = nilai2
    self.nilai3 = nilai3
    pass
  def hitung_rata_rata(self):
    hasil = (self.nilai1 + self.nilai2 + self.nilai3)/3
    return hasil
    pass
  def tanpikan_info(self):
    return print(f"Nama: {self.nama}, Rata-rata: {self.hitung_rata_rata()}")
    pass

def main():
  nama = input("Masukkan nama mahasiswa: ")
  nilai1 = float(input("Masukkan nilai ujian 1: "))
  nilai2 = float(input("Masukkan nilai ujian 2: "))
  nilai3 = float(input("Masukkan nilai ujian 3: "))

  mahasiswa = Mahasiswa(nama, nilai1, nilai2, nilai3)
  mahasiswa.tanpikan_info()

main()

