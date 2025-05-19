import pandas as pd

# Membuat DataFrame
data = {
  'Nama': ['Hadi', 'Indah', 'Joko'],
  'NIM': ['BD001', 'BD002', 'BD003'],
  'IPK': [3.7, 3.9, 3.5]
}

df = pd.DataFrame(data)
print("DataFrame yang dibuat:")
print(df)

# Menyimpan DataFrame ke Excel
df.to_excel('nilai_mahasiswa.xlsx', index=False)
print("\nData telah disimpan ke file Excel!")

# Membaca file Excel
print("\nMembaca data dari Excel:")
df_baca = pd.read_excel('nilai_mahasiswa.xlsx')
print(df_baca)

# Statistik sederhana
print("\nRata-rata IPK:", df_baca['IPK'].mean())
print("IPK tertinggi:", df_baca['IPK'].max())