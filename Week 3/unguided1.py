baris = 10
kolom = 1



for i in range (kolom,baris):
  panah = baris - i
  print(" " * panah,"*" * i, "*" *(baris -1))
  # kiri = (" " * (baris-i),"*")
  # print (kiri + kanan)

  # print (" " * (baris-i),"*"," " * i, " " * i,"*")

# for j in range (kolom, baris,2):
#   print (" " * (baris-j),"*")