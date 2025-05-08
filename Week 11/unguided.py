# Class diagram:
"""
This module provides classes to manage book and author data.
Classes:
  Penulis:
    Represents an author with a name and country of origin.
    Attributes:
      nama (str): The name of the author.
      asal_negara (str): The country of origin of the author.
    Methods:
      __init__(nama: str, asal_negara: str):
        Initializes a Penulis object with the given name and country.
      info() -> str:
        Returns a string containing the author's information.
  Buku:
    Represents a book with a title, code, price, and author.
    Attributes:
      judul (str): The title of the book.
      kode_buku (str): The unique code of the book.
      harga (float): The price of the book.
      penulis (Penulis): The author of the book.
    Methods:
      __init__(judul: str, kode_buku: str, harga: float, penulis: Penulis):
        Initializes a Buku object with the given title, code, price, and author.
      info() -> str:
        Returns a string containing the book's information, including the author's details.
Usage:
  - Create instances of the `Penulis` class to represent authors.
  - Create instances of the `Buku` class to represent books, associating them with `Penulis` instances.
  - Use the `info()` method of the `Buku` class to display detailed information about the book and its author.
Example:
  # Create authors
  # Create books
  # Display book information
"""
# 
# +-------------------+
# |     Penulis       |
# +-------------------+
# | - nama: str       |
# | - asal_negara: str|
# +-------------------+
# | + __init__(...)   |
# | + info(): str     |
# +-------------------+
# 
# +-------------------+
# |       Buku        |
# +-------------------+
# | - judul: str      |
# | - kode_buku: str  |
# | - harga: float    |
# | - penulis: Penulis|
# +-------------------+
# | + __init__(...)   |
# | + info(): str     |
# +-------------------+

class Penulis:
  def __init__(self, nama, asal_negara):
    self.nama = nama
    self.asal_negara = asal_negara

  def info(self):
    return f"Penulis: {self.nama}, Asal Negara: {self.asal_negara}"


class Buku:
  def __init__(self, judul, kode_buku, harga, penulis):
    self.judul = judul
    self.kode_buku = kode_buku
    self.harga = harga
    self.penulis = penulis

  def info(self):
    return (f"Judul Buku: {self.judul}, Kode Buku: {self.kode_buku}, "
        f"Harga: Rp{self.harga}, {self.penulis.info()}")


# Membuat data penulis
penulis1 = Penulis("Tere Liye", "Indonesia")
penulis2 = Penulis("J.K. Rowling", "Inggris")

# Membuat data buku
buku1 = Buku("Hujan", "B001", 85000, penulis1)
buku2 = Buku("Harry Potter", "B002", 150000, penulis2)

# Menampilkan informasi lengkap
print(buku1.info())
print(buku2.info())