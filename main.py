# Data was provided for.
from art import logo, vs
from game_data import data
from replit import clear
import random


PlayAgain = True
while PlayAgain == True:

  Lose = False
  Score = 0
# Function 1: Generate the names.
  def Generate():
    global Score, PostnA, PostnB
    if Score == 0:
      PostnA = data[random.randint(0,len(data))-1]
      PostnB = data[random.randint(0,len(data))-1]
      while PostnB == PostnA:
        PostnB = data[random.randint(0,len(data))-1]
    else:
      PostnA = PostnB
      PostnB = data[random.randint(0,len(data))-1]
      while PostnB == PostnA:
        PostnB = data[random.randint(0,len(data))-1]

# Function 2: Brains

  def Game():
    global Lose, Score, PostnA, PostnB
    print(logo) 
    print(f"\nYour Current score is: {Score}\n")
    Generate()

    PAName = PostnA["name"]
    PADesc = PostnA["description"]
    PACount = PostnA["country"]

    PBName = PostnB["name"]
    PBDesc = PostnB["description"]
    PBCount = PostnB["country"]

    
    PersonA = str(f"{PAName} a {PADesc} from {PACount}.")
    PersonB = str(f"{PBName} a {PBDesc} from {PBCount}.")
  

    print(f"\nCompare: {PersonA}\n\n{vs}")
    print(f"\n{PersonB}")
    
    Decider()

# Function 3: Decides who wins/game continue/ game restart.

  def Decider():
    global Score, PostnA, PostnB, PlayAgain
    Verify = False
    PAScore = PostnA["follower_count"]
    PBScore = PostnB["follower_count"]
    Guess = int(input("\nWho has more followers on instagram? 1 or 2?\n"))

    Temp = [PAScore, PBScore]
    Winner_Posn = Temp.index(max(Temp))
    
    if Guess - 1 == Winner_Posn:
      Verify = True

    if Verify ==  True:
      Score += 1
      clear()
      Game()  
    else:
      TryA = input(f"\nToo bad! You lost. Your final score is: {Score}. Go again? Y or N?\n").lower()
      if TryA == "y":
        PlayAgain = True
        clear()
      else: 
        clear()
        PlayAgain = False
        print("Hope you enjoyed! Goodbye!")

  Game()

