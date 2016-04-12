import random

def playgame():
    choice = input("Welcome to RPSLS. Would like to play with one player or two(1 or 2) \n")
    if choice == 1:
        human = guess()
        computer = findComputerNumber()
        winLose(computer,human)
    else:
        humanOne = playerOneGuess()
        humanTwo = playerTwoGuess()
        winLoseWithTwo(humanOne,humanTwo)
        
def guess():
    guess = input("Enter rock, paper, scissors, lizard, or Spock \n")
    if guess == "rock":
       human = 1
    elif guess == "Spock":
       human = 2
    elif guess == "paper":
       human = 3
    elif guess == "lizard":
        human = 4
    else:
        human = 5
    return human
    
def playerOneGuess():
    guess = input("Player 1:Enter rock, paper, scissors, lizard, or Spock \n")
    if guess == "rock":
       humanOne = 1
    elif guess == "Spock":
       humanOne = 2
    elif guess == "paper":
       humanOne = 3
    elif guess == "lizard":
        humanOne = 4
    else:
        humanOne = 5
    return humanOne
    
def playerTwoGuess():
    guess = input("Player 2:Enter rock, paper, scissors, lizard, or Spock \n")
    if guess == "rock":
       humanTwo = 1
    elif guess == "Spock":
       humanTwo = 2
    elif guess == "paper":
       humanTwo = 3
    elif guess == "lizard":
        humanTwo = 4
    else:
        humanTwo = 5
    return humanTwo
    
def winLoseWithTwo(humanOne,humanTwo):
    if (humanOne == humanTwo):
       print("tie")
       playagain()
    elif (humanOne - humanTwo)%5 == 1:
       print("Player 2 wins")
       playagain()
    else:
       print("Player 1 wins")
       playagain()
    
def findComputerNumber():
    compnum = random.randrange(1,4)
    if compnum == 1:
        print("rock")
    elif compnum == 2:
        print("Spock")
    elif compnum == 3:
        print("paper")
    elif compnum == 4:
        print("lizard")
    else:
        print("scissors")
    return compnum
    
def playagain():
    response = input("would you like to play again(yes or no)? \n")
    if response == "yes":
        playgame()
    else:
        "Thanks for playing"
        
def winLose(computer,human):
    if (computer == human):
       print("tie")
       playagain()
    elif (computer - human)%5 == 1:
       print("you've won")
       playagain()
    else:
       print("you lose")
       playagain()
       
playgame()
    
    