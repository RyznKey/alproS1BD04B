while True: # This is an infinite loop that will keep running until we break out of it
  # The loop will keep asking for input until the user types 'stop'
  reply = input("Enter text, [type 'stop' to quit:] ") # This line prompts the user for input and stores it in the variable 'reply'
  # The input is expected to be a string, and the user can type anything they want
  if reply == "stop": # This line checks if the user input is equal to the string 'stop'
    break             # If the user types 'stop', the loop will break and the program will end
  print(reply.lower())  # This line prints the user input in lowercase, regardless of how the user typed it