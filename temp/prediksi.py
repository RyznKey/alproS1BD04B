import random as rd

kategoriDua = ["exit", "motor", "gojek", "grab"]
kondisi = True
while kondisi:
  print ("=" *10, "MENU", "=" *10)
  for menu in range(len(kategoriDua)):
    print (menu, ")", kategoriDua[menu])
    
  print ("=" *10, "MENU", "=" *10)
  selectMenu = input("Pilih menu: ").lower()
  if selectMenu == "0" or selectMenu == "exit":
    print ("Keluar dari program")
    print ("=" *26)
    kondisi = False
  elif selectMenu == "1" or selectMenu == "motor":
    print ("Anda memilih motor")
    hargaBensin = 12500
    print ("Harga Bensin per liter: ", hargaBensin)
    kmPerLiter = float(input("Masukan km/liter motor anda : "))
    inputJarak = float(input("Masukan jarak tempuh : "))
    hasil = inputJarak * hargaBensin/kmPerLiter
    print ("Biaya yang harus dibayar: ", int(hasil))
  elif selectMenu == "2" or selectMenu == "gojek":
    print ("Anda memilih gojek")
    hargaPerKm = rd.randint(20000, 25000)
    print ("Harga Gojek per km: ", hargaPerKm)
    inputJarak = float(input("Masukan jarak tempuh : "))
    hasil = inputJarak * hargaPerKm
    print ("Biaya yang harus dibayar: ", int(hasil))
  elif selectMenu == "3" or selectMenu == "grab":
    print ("Anda memilih grab")
    hargaPerKm = rd.randint(20000, 25000)
    print ("Harga Grab per km: ", hargaPerKm)
    inputJarak = float(input("Masukan jarak tempuh : "))
    hasil = inputJarak * hargaPerKm
    print ("Biaya yang harus dibayar: ", int(hasil))
  else:
    print ("Pilihan tidak ada, Harap masukan dengan benar")
    print ("=" *26)
