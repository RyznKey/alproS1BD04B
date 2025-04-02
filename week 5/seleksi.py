# Program to determine grade based on score

# Read the score
nilai = int(input("Masukkan nilai: "))

# Determine the grade
if nilai >= 90:
  grade = "A"
elif nilai >= 70 and nilai < 90:
  grade = "B"
elif nilai >= 60 and nilai < 70:
  grade = "C"
elif nilai >= 50 and nilai < 60:
  grade = "D"
else:
  grade = "E"

# Display the grade
print(f"Grade: {grade}")