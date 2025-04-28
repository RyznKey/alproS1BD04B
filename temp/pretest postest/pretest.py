"""
NAMA  : AHSAN MAULANA RIZQI
NIM   : 104062400071
KELAS : S1 BD 04 B
DOSEN : ERLINA NUR ARIFANI S.T.P, M.Sc.
"""

# Pretest 1
"""
Pseudocode untuk menghitung harga setelah diskon:
1. Mulai
2. Input total pembelian
3. Jika total pembelian >= 1.000.000, maka:
      - diskon = 15%
    Jika tidak, cek jika total pembelian >= 750.000, maka:
      - diskon = 10%
    Jika tidak, cek jika total pembelian >= 500.000, maka:
      - diskon = 5%
    Jika tidak:
      - diskon = 0%
4. Hitung harga setelah diskon:
      harga setelah diskon = total pembelian - (total pembelian * diskon)
5. Output "harga setelah diskon : " + harga setelah diskon
6. Selesai
"""

# # Program menghitung harga setelah diskon

# # Input total pembelian
# total_pembelian = float(input("Masukkan total pembelian: "))       # digunakan untuk mengambil input dari user

# # Menentukan diskon
# # if statement untuk menentukan diskon 15% dengan syarat varibel total_pembelian lebih dari sama dengan 1.000.000
# if total_pembelian >= 1000000:
#   diskon = 0.15                         # diskon 15%
# # jika tidak memenuhi syarat diskon 15%, maka cek syarat diskon 10% dengan syarat varibel total_pembelian lebih dari sama dengan 750.000
# elif total_pembelian >= 750000:
#   diskon = 0.10                         # diskon 10%
# # jika tidak memenuhi syarat diskon 10%, maka cek syarat diskon 5% dengan syarat varibel total_pembelian lebih dari sama dengan 500.000
# elif total_pembelian >= 500000:
#   diskon = 0.05                         # diskon 5%
# # jika tidak memenuhi syarat diskon 5%, maka diskon adalah 0%
# else:
#   diskon = 0.0                          # diskon 0%

# # Menghitung harga setelah diskon
# harga_setelah_diskon = total_pembelian - (total_pembelian * diskon) # rumus untuk menghitung harga setelah diskon

# # Output hasil
# # menampilkan harga setelah diskon dengan format ribuan dan dua angka di belakang koma
# # :.2f adalah format untuk menampilkan dua angka dibelakan koma
# print(f"Harga setelah diskon: Rp{harga_setelah_diskon:,.2f}")       

# Pretest 2

"""
pseudocode untuk konversi nilai ke grade:
1. Mulai
2. Input nilai
3. Jika nilai >= 80, maka:
        - grade = 'A'
    Jika tidak, cek jika nilai >= 70, maka:
        - grade = 'B'
    Jika tidak, cek jika nilai >= 60, maka:
        - grade = 'C'
    Jika tidak, cek jika nilai >= 50, maka:
        - grade = 'D'
    Jika tidak:
        - grade = 'E'
4. Output "Grade" + str(grade)
5. Selesai
"""

# Program konversi nilai ke grade
nilai = float(input("Masukkan nilai: "))  # Digunakan untuk mengambil input dari user

# Menentukan grade
# if statement untuk menentukan grade A dengan syrat vaariavel nilai memiliki value lebih dari sama dengan 80
if nilai >= 80:                           
  grade = 'A'
# Jika tidak memenuhi syarat grade A, maka cek syarat grade B dengan syarat nilai lebih dari sama dengan 70 dan kurang dari 80
elif nilai >= 65 and nilai < 80:
  grade = 'B'
# Jika tidak memenuhi syarat grade B, maka cek syarat grade C dengan syarat nilai lebih dari sama dengan 50 dan kurang dari 65
elif nilai >= 50 and nilai < 65:
  grade = 'C'
# Jika tidak memenuhi syarat grade C, maka cek syarat grade D dengan syarat nilai lebih dari sama dengan 40 dan kurang dari 50
elif nilai >= 40 and nilai < 50:
  grade = 'D'
# Jika tidak memenuhi syarat grade D, maka nilai di bawah 40 adalah grade E
else:
  grade = 'E'

# Output grade
print(f"Grade: {grade}")               # menampilkan grade