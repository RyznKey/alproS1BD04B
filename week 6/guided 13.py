lines =list() 
testAnswer = input("Apakah Anda ingin memasukan baris ke list? (y): ") # jika pengguna ingin memasukkan baris ke list ketik "y"
while testAnswer == "y":
    line = input("Masukkan baris teks: ")
    lines.append(line) #digunakan untuk menambahkan item ke akhir sebuah list
    testAnswer = input("Apakah Anda ingin menambahkan baris lagi? (y): ")
print ("Baris yang telah anda masukkan adalah: ")
for i in lines: # Ketika pengguna mengetik selain "y", semua baris yang telah dimasukkan akan ditampilkan
    print(i)