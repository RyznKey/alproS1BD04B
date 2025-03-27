def segitiga(sisi):
  count = 1 # jumlah bintang
  spasi = int(sisi/2) # spasi awal
  jarak = 0
  while True:
    # jika count ganjil, print bintang
    if count%2:
      # print(jarak)
      if count == 1:  
        print(" " * spasi + "*")  
      elif count == sisi or count -1 == sisi:  
        sisi /= 3
        jarak -= 1
        print("*" * int(sisi) + "1" * int(jarak) + "*" * int(sisi))
      else:  
        print(" " * spasi + "*" + " " * (count - 2) + "*")  
      spasi -=1
      jarak +=1 
      # print(jarak)
      count +=1
    else:
      count +=1
      continue
    # jika jumlah bintang sudah mencapai sisi, break
    if count > sisi:
      break

def persegi(sisi):
  if sisi % 2:
    sisi = int(sisi/3)
    for i in range(sisi):
      print(" " * int(sisi/2), '*' , " " * int(sisi/2), "*")
    print(" " * int((sisi/2)), '*' * (sisi+2))
  else:
    sisi = int(sisi/2)
    for i in range(sisi):
      print(" " * int(sisi/3), '*' , " " * int(sisi/2+1), "*")
    print(" " * int((sisi/2-1)), '*' * (sisi+2))

# Main Program
# panjang = int(input("Masukkan panjang sisi: "))
panjang = 9
segitiga(panjang)
persegi(panjang)
panjang = 10
segitiga(panjang)
persegi(panjang)