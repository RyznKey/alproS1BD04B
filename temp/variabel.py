# proses masukan data ke dalam variabel

name = "ahsan maulana rizqi"
print (name)
# nilai data pada variabel dapat diubah 
umur = 20 #nilai awal
print (umur) # cetak nilai umur
print (type (umur)) # cetak & cek tipe data umur
umur = "dua puluh lima" # nilai yg sudah di ubah
print (umur) # cetak nilai umur
print (type (umur)) # cetak & cek tipe data umur

namaDepan = "ahsan"
namaBelakang = "maulana"
nama = namaDepan + " " + namaBelakang
umur = 22
hobi = "berenang"
print ("Biodata \n", nama, "\n", umur, "\n", hobi)
# contoh variable lainnya
iniVariabel = "Halo"
ini_juga_variabel = "Hai"
_iniJugaVariabel = "Hi"
iniVariabel222 = "Bye"

panjang = 10
lebar = 5
luas = panjang * lebar
print (luas)
i = 2
print ((2+3*i)+(1-2*i))

rusuk = 10.5
luasPermukaan = 6 * rusuk ** 2
volume = rusuk ** 3
print (luasPermukaan)
print (volume)

# variable 
a,b = -1,10 
if (a<=0 and b >= 0):
    print (True)
else :
  print (False)