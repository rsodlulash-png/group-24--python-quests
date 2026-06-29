#!/usr/bin/python3
def ask_for_age():
    age = int(input("enter your age: "))
    return age
def can_they_vote(age):
    if age >= 18:
        return("you can vote")
    else:
        return("you are not eligible to vote")
print(can_they_vote(ask_for_age())) 
