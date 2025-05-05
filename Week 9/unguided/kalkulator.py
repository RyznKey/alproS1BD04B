import formula as fm

while True:
  print("\n========Kalkulator Sederhana========")
  print("format kalkulator adalah a operator b")
  a,op,b = input("Masukkan operasi (a op b): ").split()
  a = float(a)
  b = float(b)
  if op == "+":
    print("Hasil: ", fm.tambah(a,b))
  elif op == "^":
    print("Hasil: ", fm.pangkat(a,b))
  elif op == "%":
    if b != 0:
      print("Hasil: ", fm.modulus(a,b))
    else:
      print("Error: ", fm.modulus(a,b))
  else:
    print("Operator tidak valid!")
  print ("=" * 35)
  lanjut = input("Apakah Anda ingin melanjutkan? (y/n): ")
  if lanjut.lower() != "y":
    print("Terima kasih telah menggunakan kalkulator sederhana ini!")
    break