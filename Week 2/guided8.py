glass_a = "susu"
glass_b = "jus"

print ("Sebelum ditukar isi gelas : ")
print (f"gelas berisi : {glass_a}")
print (f"gelas berisi : {glass_b}")

glass_a,glass_b = glass_b,glass_a

print ("Setelah ditukar isi gelas : ")
print (f"gelas berisi : {glass_a}")
print (f"gelas berisi : {glass_b}")