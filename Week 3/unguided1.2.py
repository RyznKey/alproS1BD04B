# inisialisasi variabel
sisi = 9
spasi = int(sisi/2) # spasi awal
# loop untuk pola segitiga
for count in range(1, sisi + 1,2):
  if count == 1:
      print(" " * spasi + "*")
  elif count == sisi:
    sisi /= 3
    count /= 3
    print("*" * int(sisi) + " " * int(count) + "*" * int(sisi))
  else:
    print(" " * spasi + "*" + " " * (count - 2) + "*")
  spasi -= 1
# loop untuk pola persegi panjang
for i in range(int(sisi)):
  print(" " * int(sisi/2), '*' , " " * int(sisi/2), "*")
print(" " * int(sisi/2), '*' * int(sisi+2))