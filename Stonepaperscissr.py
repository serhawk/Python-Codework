####This is a if, elif, else practice
import random
while True:
    options = ["stone", "paper", "scissor"]
    computer = random.choice(options)
    player = str(input("Enter a value: stone? paper? scissor?"))
    if computer == player:
        print("Draw")
    elif computer == "stone":
      if player == "paper":
         print ("Computer:",computer)
         print ("Player:", player)
         print ("Computer wins")
      if player == "scissor":
         print ("computer:", computer)
         print ("Player:", player)
         print ("Computer Wins")
    elif computer == "scissor" :
      if player == "paper":
         print ("computer:", computer)
         print ("Player:", player)
         print ("Computer Wins")
      if player == "stone":
         print ("computer:", computer)
         print ("Player:", player)
         print ("Player Wins")
    elif computer == "paper":
      if player == "stone":
         print("computer:", computer)
         print("Player:", player)
         print("Player Wins")
      if player == "scissor":
         print("computer:", computer)
         print("Player:", player)
         print("Player Wins")
    play_again = input("Play Again Y/N ?:").lower()
    if play_again == "N":
       break
print("Good Bye")