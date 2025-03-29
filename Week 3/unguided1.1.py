sisi = 9
spasi = sisi // 2  # Spasi awal untuk segitiga

# Loop untuk pola segitiga
for count in range(1, sisi, 2):  # Menggunakan step 2 untuk pola segitiga
    if count == 1:
        print(" " * spasi + "*")  # Baris pertama segitiga
    elif count == sisi - 1:
        print("*" * (count) + " " * 3 + "*" * (count))  # Baris terakhir segitiga dengan tiga bintang di tengah
    else:
        print(" " * spasi + "*" + " " * (count - 2) + "*")  # Baris tengah segitiga
    spasi -= 1  # Mengurangi spasi setiap kali ke baris berikutnya

# Loop untuk pola persegi panjang (bagian bawah panah)
for i in range(sisi // 3):  # Tinggi persegi panjang disesuaikan
    print(" " * (sisi // 3) + "*" + " " * (sisi // 3) + "*")  # Dua bintang dengan spasi tengah

# Baris terakhir persegi panjang
print(" " * (sisi // 3) + "*" * (sisi + 2))  # Baris penuh dengan bintang
