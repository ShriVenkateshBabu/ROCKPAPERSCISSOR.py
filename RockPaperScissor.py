# userinput = input("1: throw rock paper scissor\n")
# userinput2 = input("2: throw rock paper scissor\n")
# rock = "rock"
# paper = "paper"
# scissor = "scissor"
# winorloss  = "win"
# if userinput ==userinput2:
#  print("Tie")
# if userinput=="rock" and userinput2== "paper" :
#  winorloss = "loss for rock"
#  print(winorloss)
# if userinput=="rock" and userinput2== "scissor" :
#  winorloss = "loss for scissor"
#  print(winorloss)
# if userinput=="paper" and userinput2== "scissor" :
#  winorloss = "loss for paper"
#  print(winorloss)
# if userinput=="paper" and userinput2== "rock" : 
#  winorloss = "loss for rock"
#  print(winorloss)
# if userinput=="scissor" and userinput2== "rock" : 
#  winorloss = "loss for scissor"
#  print(winorloss)
# if userinput=="scissor" and userinput2== "paper" :
#  winorloss = "loss for paper"
#  print(winorloss)
# else :
#  print("invlaid syuntax")
# import random
# import sys

# print("")

# PlayerChoice = input("Enter......\n 1 - for rock \n 2 - scissor \n 3 - paper\n")

# player = int(PlayerChoice)

# if player > 3 or player < 0 :
#     sys.exit("you must enter 1,2 ,3 ")

# ComputerChoice = random.choice("123")

# computer = int(ComputerChoice)
# choices = {1:"rock", 2:"scissor",3:"paper"}
# print(".........................")
# print("Player Choice" +"  = "+ f"{choices[player]}" )
# print("Computer Choose" + "  = " + f"{choices[computer]}")
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>")

# if player == 1 and computer == 2:
#     print("you win 👍")
# elif player == 2 and computer == 3:
#     print("you win 👍")
# elif player ==3 and computer == 1 :
#     print("you win 👍")
# elif player==computer:
#     print("GAME TIE>>>>🙌")
# else:
#     print("Computer Wins")

import random
import sys
from enum import Enum

class RPS(Enum):
    ROCK = 1
    SCISSOR = 2
    PAPER = 3

print("")

PlayerChoice = input("Enter......\n 1 - for rock \n 2 - scissor \n 3 - paper\n")

player = int(PlayerChoice)

if player > 3 or player < 0 :
    sys.exit("you must enter 1,2 ,3 ")

ComputerChoice = random.choice("123")

computer = int(ComputerChoice)
# choices = {1:"rock", 2:"scissor",3:"paper"}
print(".........................")
print("Player Choice" +"  = " + str(RPS(player)).replace("RPS.",""))
print("Computer Choose" + "  = " + str(RPS(computer)).replace("RPS.","") )
print(">>>>>>>>>>>>>>>>>>>>>>>>>>")

if player == 1 and computer == 2:
    print("you win 👍")
elif player == 2 and computer == 3:
    print("you win 👍")
elif player ==3 and computer == 1 :
    print("you win 👍")
elif player==computer:
    print("GAME TIE>>>>🙌")
else:
    print("Computer Wins")