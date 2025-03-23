
# # program yang meminta inputan dari user berupa 
# nama = str(input ("Masukkan nama Anda: "))          # input nama
# NIM = int(input ("Masukkan NIM Anda: "))            # input NIM
# alamat = str(input ("Masukkan alamat Anda: "))      # input alamat
# tanggal_lahir = str(input ("Masukkan tanggal lahir Anda: ")) # input tanggal lahir
# jenis_kelamin = str(input ("Masukkan jenis kelamin Anda: ")) # input jenis kelamin
# umur = int(input ("Masukkan umur Anda: "))          # input umur
# tinggi = float(input ("Masukkan tinggi Anda: "))    # input tinggi
# berat = float(input ("Masukkan berat Anda: "))      # input berat

# # output data yang telah diinputkan
# print ("Nama saya adalah", nama)
# print ("NIM saya adalah", NIM)
# print ("Alamat saya adalah", alamat)
# print ("Tanggal lahir saya adalah", tanggal_lahir)
# print ("Jenis kelamin saya adalah", jenis_kelamin)
# print ("Umur saya adalah", umur)
# print ("Tinggi saya adalah", tinggi)
# print ("Berat saya adalah", berat)

class Mahasiswa:
  def __init__(self, nama, NIM, alamat, tanggal_lahir, jenis_kelamin, umur, tinggi, berat):
    self.nama = nama
    self.NIM = NIM
    self.alamat = alamat
    self.tanggal_lahir = tanggal_lahir
    self.jenis_kelamin = jenis_kelamin
    self.umur = umur
    self.tinggi = tinggi
    self.berat = berat

  def __str__(self):
    display = f"""
{"="*10} Data Mahasiswa {"="*10}
nama            : {self.nama}
NIM             : {self.NIM}
alamat          : {self.alamat}
tanggal lahir   : {self.tanggal_lahir}
jenis kelamin   : {self.jenis_kelamin}
umur            : {self.umur}
tinggi          : {self.tinggi}
berat           : {self.berat}
"""
    return display

# membuat objek mahasiswa
nama = "ahsan maulana"
NIM = 123456
alamat = "Jl. Jalan"
tanggal_lahir = "01-01-2000"
jenis_kelamin = "Laki-laki"
umur = 21
tinggi = 170
berat = 60

mhs = Mahasiswa(nama, NIM, alamat, tanggal_lahir, jenis_kelamin, umur, tinggi, berat)  
print(mhs) # print objek mahasiswa