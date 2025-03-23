# fungsi untuk membuat segitiga
def segitiga(sisi):
  count = 1 # jumlah bintang
  spasi = int(sisi/2) # spasi awal
  while True:
    # jika count ganjil, print bintang
    if count%2:
      print(" " * spasi + '*'*count)
      spasi -=1
      count +=1
    else:
      count +=1
      continue
    # jika jumlah bintang sudah mencapai sisi, break
    if count > sisi:
      break

# fungsi untuk membuat persegi
def persegi(sisi):
  sisi = int(sisi/2)
  for i in range(int(sisi)):
    if sisi % 2: # jika sisi ganjil
      print(" " * int(sisi/2), f'{i}' * sisi)
    else:
      print(" " * int(sisi/2), '*' * (sisi-1))

# Main Program
panjang = int(input("Masukkan panjang sisi: "))
segitiga(panjang)
persegi(panjang)