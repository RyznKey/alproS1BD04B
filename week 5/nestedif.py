# nested if statements
umur = 38 #identifier umur
if umur >= 11: # statement pertama jika umur lebih dari 11
  print ("tiket tersedia") # tampilkan tiket tersedia
  if umur <= 20 or umur >= 60: # nested if statement jika umur kurang dari 20 atau lebih dari 60
    print("harga tiket 35.000") # tampilkan harga tiket 35.000
  else: # jika umur tidak memenuhi syarat diatas
    print("harga tiket 50.000") # tampilkan harga tiket 50.000
else: # jika umur kurang dari 11
  print("tiket tidak tersedia") # tampilkan tiket tidak tersedia
