lines = list()  # Digunakan untuk menyimpan baris teks yang dimasukkan oleh pengguna
testAnswer = input("Apakah Anda ingin memasukan baris ke list? (y): ") # jika pengguna ingin memasukkan baris ke list ketik "y"
while testAnswer == "y": # jika pengguna mengetik "y" maka program akan meminta pengguna untuk memasukkan baris teks
    line = input("Masukkan baris teks: ") # meminta pengguna untuk memasukkan baris teks
    lines.append(line) #digunakan untuk menambahkan item ke akhir sebuah list
    testAnswer = input("Apakah Anda ingin menambahkan baris lagi? (y): ")
print ("Baris yang telah anda masukkan adalah: ") # jika pengguna mengetik selain "y"
for line in lines: # Ketika pengguna mengetik selain "y", semua baris yang telah dimasukkan akan ditampilkan
    print(line) # menampilkan semua baris yang telah dimasukkan