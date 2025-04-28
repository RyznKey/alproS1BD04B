def descibe_pet (animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

descibe_pet("hamster", "harry")
descibe_pet(animal_type= "hamster", pet_name = "harry")

# devault valuable parameter

def descibe_pet (pet_name, animal_type = "dog"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# argument akan disimpan di variable pet_name
descibe_pet("harry") # use default dog for animal_type

#  using a function with looping

def greet_user(names):
  """function to greet each user in the list"""
  for name in names:
    print(f"Hello, {name.title()}!")

# list of users
usernames = ["alice", "bob", "charlie"]

# function call with list of usernames
greet_user(usernames)

"""
penjelasan kode diatas:

nama fungsi nya adalah greet_user, dan parameter  nya adalah names
for  name in names: artinya untuk setiap nama dalam list names, lakukan perintah dibawahnya

usernames = ["alice", "bob", "charlie"] adalah list yang berisi nama-nama user
graet_user(usernames) adalah pemanggilan fungsi greet_user dengan argumen usernames, yang akan mencetak pesan sapaan untuk setiap nama dalam list usernames

argument username dikirim yang akan disimpan di variable names, dan akan di looping untuk setiap nama dalam list names
"""



def rectangle_area(length, width):
  """Calculate the area of a rectangle."""
  return length * width

def triangle_area(base, height):
  """Calculate the area of a triangle."""
  return 0.5 * base * height

# Example usage
rect_area = rectangle_area(10, 5)  # Rectangle with length=10 and width=5
tri_area = triangle_area(6, 4)     # Triangle with base=6 and height=4

# Multiply the areas
result = rect_area * tri_area
print(f"The result of the rectangle area multiplied by the triangle area is: {result}")