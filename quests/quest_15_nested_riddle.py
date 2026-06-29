# Ask the user for their first choice

direction = input("Do you go 'left' or 'right'? ").strip().lower()

# First layer of checking
if direction == "left":
     # This code only runs if they typed 'left'
     
   action = input("You reach a river. Do you 'swim' or 'wait'?").strip().lower()
   
   if action == "swim":
       print("Congratulations!You swam across and found a hidden treasure chest!")
    else:
       print("You waited too long and a wild beast chased you away.")
  else:
      # This runs if they typed 'right' or anything else
       print("You walked into a dark forest and got lost. Game over")
