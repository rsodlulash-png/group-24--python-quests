#!/usr/bin/python3
total_gold = 27
friends = 4
gold_per_friend = total_gold // friends   
goblin_keeps = total_gold % friends
print(f"each friend gets {gold_per_friend} pieces")
print(f"the goblin keeps {goblin_keeps} piecees")
