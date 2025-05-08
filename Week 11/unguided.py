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
  # Constructor to initialize the author's name and country of origin
  def __init__(self, nama, asal_negara):
    self.nama = nama  # Author's name
    self.asal_negara = asal_negara  # Author's country of origin

  # Method to return author's information as a string
  def info(self):
    return f"Penulis: {self.nama}, Asal Negara: {self.asal_negara}"


class Buku:
  # Constructor to initialize the book's title, code, price, and author
  def __init__(self, judul, kode_buku, harga, penulis):
    self.judul = judul  # Book title
    self.kode_buku = kode_buku  # Unique book code
    self.harga = harga  # Book price
    self.penulis = penulis  # Author of the book (Penulis object)

  # Method to return book's information, including author's details, as a string
  def info(self):
    return (f"Judul Buku: {self.judul}, Kode Buku: {self.kode_buku}, "
        f"Harga: Rp{self.harga}, {self.penulis.info()}")


# Creating author data
penulis1 = Penulis("Tere Liye", "Indonesia")  # Author 1
penulis2 = Penulis("J.K. Rowling", "Inggris")  # Author 2

# Creating book data
buku1 = Buku("Hujan", "B001", 85000, penulis1)  # Book 1 associated with Author 1
buku2 = Buku("Harry Potter", "B002", 150000, penulis2)  # Book 2 associated with Author 2

# Displaying complete information about the books
print(buku1.info())  # Print information of Book 1
print(buku2.info())  # Print information of Book 2