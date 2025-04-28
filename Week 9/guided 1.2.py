def luasLingkaran():
  jari_jari = 2
  phi = 3.14
  luas = phi * jari_jari * jari_jari
  return luas

hasil = luasLingkaran() # nilai hasil dari variabel harus disimpan ke suatu variabel
print (hasil)

print (luasLingkaran()) # atau langsung dicetak dengan print

"""
penjelasan:

nama fungsi : luasLingkaran
body fungsi :  jari_jari = 2, phi = 3.14, luas = phi * jari_jari * jari_jari
return: luas

variabel hasil: menyimpan nilai dari fungsi luasLingkaran
print(hasil): mencetak nilai dari variabel hasil
print(luasLingkaran()): mencetak nilai dari fungsi luasLingkaran langsung
"""