# Soal nomor 1

# Meminta input dari pengguna dan menyimpannya dalam variabel "decimal"
decimal = int(input("Masukkan bilangan desimal: "))

# Mengonversi bilangan desimal ke biner dan menampilkannya
biner = bin(decimal)[2:]  # [2:] untuk menghilangkan prefix '0b'
print(f"Bilangan biner: {biner}")

# Mengonversi bilangan desimal ke oktal dan menampilkannya
oktal = oct(decimal)[2:]  # [2:] untuk menghilangkan prefix '0o'
print(f"Bilangan oktal: {oktal}")
