# Latihan 3 - Polimorfisme = method sama dengan nama yang berbeda pada class yang berbeda
# Polimorfisme adalah kemampuan untuk menggunakan metode yang sama pada objek yang berbeda
class Hewan: 
  def bersuara(self): # memanggil suara hewan
    return "Hewan bersuara" # method bersuara dari class Hewan

class Anjing(Hewan): # class Anjing adalah subclass dari class Hewan
  def bersuara(self): # override method bersuara dari class Hewan
    return "Guk guk!" # method bersuara dari class Hewan di override dengan method bersuara dari class Anjing

class Kucing(Hewan): # class Kucing adalah subclass dari class Hewan
  def bersuara(self): # override method bersuara dari class Hewan
    return "Meong!"  # method bersuara dari class Hewan di override dengan method bersuara dari class Kucing

# Fungsi dengan polimorfisme
def suara_hewan(hewan): # parameter hewan bisa diisi dengan objek dari class Hewan, Anjing, atau Kucing
  print(hewan.bersuara()) # memanggil method bersuara dari class Hewan, Anjing, atau Kucing

# Penggunaan
hewan = Hewan() # membuat objek variable hewan dari class Hewan 
anjing = Anjing() # membuat objek variable anjing dari class Anjing
kucing = Kucing() # membuat objek variable kucing dari class Kucing

suara_hewan(hewan)  # Hewan bersuara
suara_hewan(anjing) # Guk guk!
suara_hewan(kucing) # Meong!