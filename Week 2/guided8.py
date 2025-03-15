# variabel
glass_a = "susu"
glass_b = "jus"

# sebelum
print ("Sebelum ditukar isi gelas")
print (f"gelas berisi : {glass_a}")
print (f"gelas berisi : {glass_b}")

# variabel yang ditukar
glass_a,glass_b = glass_b,glass_a

# setelah
print ("Setelah ditukar isi gelas")
print (f"gelas berisi : {glass_a}")
print (f"gelas berisi : {glass_b}")