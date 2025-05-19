import json

# Data untuk ditulis ke JSON
produk = {
  "nama": "Laptop Bisnis Pro",
  "harga": 15000000,
  "spesifikasi": {
    "prosesor": "Intel Core i7",
    "ram": "16GB"
  },
  "stok": 25
}

# Menulis ke file JSON
with open('produk.json', 'w') as file:
  json.dump(produk, file, indent=4)

print("Data telah ditulis ke file JSON!")

# Membaca dari file JSON
with open('produk.json', 'r') as file:
  data = json.load(file)

print("\nData dari produk.json:")
print(f"Nama produk: {data['nama']}")
print(f"Harga: Rp{data['harga']}")
print(f"Prosesor: {data['spesifikasi']['prosesor']}")
print(f"RAM: {data['spesifikasi']['ram']}")
print(f"Stok tersedia: {data['stok']}")