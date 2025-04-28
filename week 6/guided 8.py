i = 0 # Inisialisasi variabel i
while i < 8: # Looping selama i kurang dari 8
  i += 1     # Menambah nilai i setiap iterasi
  if i == 6: # Jika i yang dimasukkan adalah 6, lanjutkan ke iterasi berikutnya
    continue # continue statement untuk melanjutkan ke iterasi berikutnya
  print(i, end=' ') # Menampilkan nilai i yang tidak sama dengan 6
print()