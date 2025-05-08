# Latihan 3 - Polimorfisme
class Hewan:
  def bersuara(self):
    return "Hewan bersuara"

class Anjing(Hewan):
  def bersuara(self):
    return "Guk guk!"

class Kucing(Hewan):
  def bersuara(self):
    return "Meong!"

# Fungsi dengan polimorfisme
def suara_hewan(hewan):
  print(hewan.bersuara())

# Penggunaan
hewan = Hewan()
anjing = Anjing()
kucing = Kucing()

suara_hewan(hewan)  # Hewan bersuara
suara_hewan(anjing) # Guk guk!
suara_hewan(kucing) # Meong!