#!/usr/bin/python3
def choose_location():
    adventure = input("Choose Your Own Adventure Dubai or forest: ")
    return adventure
def different_endings(adventure):
    if adventure == "Dubai":
        return("you found the treasure in dubai")
    elif adventure == "forest":
        return("there is no treasure in the forest")
    else:
        return("You are lost")
print(different_endings(choose_location()))    

