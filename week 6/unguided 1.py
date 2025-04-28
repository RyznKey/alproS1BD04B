while True:
  print("Kalkulator Sederhana")
  print("Masukkan 0 pada operator untuk keluar dari program.")
  
  try:
    # Input bilangan pertama
    bilangan1 = float(input("Masukkan bilangan pertama: "))
    
    # Input operator
    operator = input("Masukkan operator (*, /, +, -): ")
    
    # Jika operator adalah 0, keluar dari program
    if operator == "0":
      print("Program dihentikan.")
      break
    
    # Input bilangan kedua
    bilangan2 = float(input("Masukkan bilangan kedua: "))
    
    # Proses perhitungan berdasarkan operator
    if operator == "*":
      hasil = bilangan1 * bilangan2
      print(f"Hasil: {bilangan1} * {bilangan2} = {hasil}")
    elif operator == "/":
      if bilangan2 == 0:
        print("Error: Tidak dapat membagi dengan 0.")
      else:
        hasil = bilangan1 / bilangan2
        print(f"Hasil: {bilangan1} / {bilangan2} = {hasil}")
    elif operator == "+":
      hasil = bilangan1 + bilangan2
      print(f"Hasil: {bilangan1} + {bilangan2} = {hasil}")
    elif operator == "-":
      hasil = bilangan1 - bilangan2
      print(f"Hasil: {bilangan1} - {bilangan2} = {hasil}")
    else:
      print("Operator tidak valid. Silakan masukkan operator yang benar (*, /, +, -).")
  except ValueError:
    print("Input tidak valid. Masukkan angka yang benar.")
  
  print()  # Baris kosong untuk pemisah antar iterasi