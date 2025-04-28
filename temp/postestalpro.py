# Soal nomor 1

# Meminta input dari pengguna dan menyimpannya dalam variabel "decimal"
decimal = int(input("Masukkan bilangan desimal: "))

# Mengonversi bilangan desimal ke biner dan menampilkannya
biner = bin(decimal)  
print(f"Bilangan biner: {biner}")

# Mengonversi bilangan desimal ke oktal dan menampilkannya
oktal = oct(decimal) 
print(f"Bilangan oktal: {oktal}")

# Soal nomor 3

while True:
  print("""
pilih menu untuk menghitung luas
0. keluar
1. segitiga
2. trapesium
""")
  menu = input("masukkan menu: ")                      # input user untuk memilih menu
  if menu == "1": 
    alas = float(input("masukkan alas: "))             # input alas segitiga
    tinggi = float(input("masukkan tinggi: "))         #input tinggi segitiga
    luas = (alas * tinggi) / 2                         # rumus luas segitiga
    print(f"luas segitiga adalah {luas}")              # menampilakn hasil luas segitiga
  elif menu == "2":
    a = float(input("masukkan panjang sisi atas: "))   # input alas atas trapesium
    b = float(input("masukkan panjang sisi bawah: "))  # input alas bawah trapesium
    tinggi = float(input("masukkan tinggi: "))         # input tinggi trapesium
    luas = ((a + b) * tinggi) / 2                      # rumus luas trapesium
    print(f"luas trapesium adalah {luas}")             # menampilakn hasil luas trapesium
  elif menu == "0":
    print("keluar")                                    # menampilkan pesan keluar
    break                                              # keluar dari loop
  else:
    print("menu tidak ada")                            # jika menu tidak ada


# Soal nomor 5

quiz = int(input("masukkan nilai quiz: "))                # input nilai quiz
uts = int(input("masukkan nilai uts: "))                  # input nilai uts
uas = int(input("masukkan nilai uas: "))                  # input nilai uas

# rumus nilai akhir
nilai_akhir = (quiz * 0.25) + (uts * 0.35) + (uas * 0.4)  
# rumus rata-rata
rata_rata = (quiz + uts + uas) / 3                        

print (f"rata-rata adalah {rata_rata}")                   # menampilkan rata-rata

# hasil lulus atau gagal dari rata rata
if rata_rata >= 60:
  print("LULUS")                                          # jika rata-rata >= 60 maka lulus
else:
  print("GAGAL")                                          # jika rata-rata < 60 maka tidak lulus

# Hasil Huruf Mutu Dari Nilai Akhir
if nilai_akhir >= 0 and nilai_akhir < 45:                 # jika nilai akhir kurang dari 45 dan lebih dari sama dengan 0
  print("HURUF MUTU : E")
elif nilai_akhir >= 45 and nilai_akhir < 55:              # jika nilai akhir kurang dari 55 dan lebih dari sama dengan 45
  print ("HURUF MUTU : D")
elif nilai_akhir >= 55 and nilai_akhir < 68:              # jika nilai akhir kurang dari 68 dan lebih dari sama dengan 55 
  print ("HURUF MUTU : C")
elif nilai_akhir >= 68 and nilai_akhir < 80:              # jika nilai akhir kurang dari 80 dan lebih dari sama dengan 68
  print ("HURUF MUTU : B")
elif nilai_akhir >= 80 and nilai_akhir <= 100:            # jika nilai akhir kurang dari 100 dan lebih dari sama dengan 80
  print ("HURUF MUTU : A")