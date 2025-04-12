# Program to determine grade based on score
# Read the score
nilai = int(input("Masukkan nilai: ")) #identifier value with user input
# Determine the grade
if nilai >= 90: # frist if statement to check the score, if the score is greater than or equal to 90
  grade = "A" # assign grade A
elif nilai >= 70 and nilai < 90: # # second if statement to check the score, if the score is greater than or equal to 70
  grade = "B" # assign grade B
elif nilai >= 60 and nilai < 70: # # third if statement to check the score, if the score is greater than or equal to 60
  grade = "C" # assign grade C
elif nilai >= 50 and nilai < 60: # # fourth if statement to check the score, if the score is greater than or equal to 50
  grade = "D" # assign grade D
else: # # else statement to check the score, if the score not meet the above conditions
  grade = "E" # assign grade E
# Display the grade   
print(f"Grade: {grade}") 