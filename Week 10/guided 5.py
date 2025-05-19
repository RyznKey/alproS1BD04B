# Define a class to represent a category
class Kategori:
  def __init__(self, nama):
    # Initialize the category with a name
    self.nama = nama

# Define a class to represent a product
class Produk:
  def __init__(self, kode, nama, harga, kategori):
    # Initialize the product with a code, name, price, and category
    self.kode = kode
    self.nama = nama
    self.harga = harga
    self.kategori = kategori

  # Method to display product information
  def info(self):
    print(f"Kode: {self.kode}")  # Display product code
    print(f"Nama: {self.nama}")  # Display product name
    print(f"Harga: Rp{self.harga}")  # Display product price
    print(f"Kategori: {self.kategori.nama}")  # Display category name

# Example usage
if __name__ == "__main__":
  # Create categories
  kat_elektronik = Kategori("Elektronik")  # Create an "Elektronik" category
  kat_pakaian = Kategori("Pakaian")  # Create a "Pakaian" category

  # Create products
  laptop = Produk("P001", "Laptop Gaming", 8000000, kat_elektronik)  # Create a laptop product
  kaos = Produk("P002", "Kaos Skena", 150000, kat_pakaian)  # Create a t-shirt product

  # Display product information
  print("=== Info Produk 1 ===")
  laptop.info()  # Display information for the laptop
  print("\n=== Info Produk 2 ===")
  kaos.info()  # Display information for the t-shirt