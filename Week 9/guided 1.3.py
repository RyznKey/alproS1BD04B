def volumePersegi(p,l,t):
  volume = p * l * t
  return volume

kardus = volumePersegi(13, 5, 10)
dadu = volumePersegi (2, 2, 2)

print (kardus)
print (dadu)

"""
penjelasan:

kode diatas untuk menghitung volume persegi dari dua benda yaitu kardus dan dadu

memiliki fungsi yaitu volumePersegi dengan parameter p, l, t
return volume untuk mengembalikan nilai volume

nama fungsi : volumePersegi
prameter fungsi : p, l, t
body fungsi : volume = p * l * t, return volume

kardus: menyimpan nilai dari fungsi volumePersegi dengan parameter 13, 5, 10
volume perseginya yaitu 13 * 5 * 10 = 650
dadu: menyimpan nilai dari fungsi volumePersegi dengan parameter 2, 2, 2
volume perseginya yaitu 2 * 2 * 2 = 8


untuk mengeluarkan nilai butuh pemanggilan 
print(kardus): mencetak nilai dari variabel kardus
print(dadu): mencetak nilai dari variabel dadu

hasil:
kardus = 650
dadu = 8
"""