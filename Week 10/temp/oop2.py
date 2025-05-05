class MobileSedan:
  def __init__(self):
    self.brand = "Toyota"
    self.model = "Camry"
    self.year = 2020
    self.color = "Blue"
    self.mileage = 15000
    self.price = 20000
#  constructor 
  def maju(self):
    print(f'Sedan {self.brand} warna {self.color} maju... Brum Brum Brum')

  def mundur(self):
    print(f'Sedan {self.brand} warna {self.color} mundur... Drun Drun Drun')

  def berhenti(self):
    print(f'Sedan {self.brand} warna {self.color} berhenti... Bruk')


# membuat instance dari class MobileSedan
mobilSedan = MobileSedan()
mobilSedan.maju()
mobilSedan.mundur()
mobilSedan.berhenti()

