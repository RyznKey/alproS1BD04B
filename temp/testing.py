import math

def menu():
  print("===== MENU =====")
  print("1. Menghitung luas persegi panjang")
  print("2. Menghitung keliling persegi panjang")
  print("3. Menghitung diagonal persegi panjang")
  print("================")
  pilihan = int(input("Masukkan Pilihan Anda: "))
  return pilihan

def hitung_luas(p, l):
  return p * l

def hitung_keliling(p, l):
  return 2 * p + 2 * l

def hitung_diagonal(p, l):
  return math.sqrt(p * p + l * l)


while True:
  pilihan = menu()
  if pilihan in [1, 2, 3]:
    p = float(input("Masukkan panjang (P): "))
    l = float(input("Masukkan lebar (L): "))
    
  if pilihan == 1:
    print(f"Luas persegi panjang = {hitung_luas(p, l)}")
  elif pilihan == 2:
    print(f"Keliling persegi panjang = {hitung_keliling(p, l)}")
  elif pilihan == 3:
    print(f"Panjang diagonal persegi panjang = {hitung_diagonal(p, l)}")
  else:
    print("Pilihan tidak valid. Silakan coba lagi.")
    
  lanjut = input("Apakah Anda ingin melanjutkan? (y/n): ").lower()
  if lanjut != 'y':
    print("Terima kasih telah menggunakan program ini.")
    break