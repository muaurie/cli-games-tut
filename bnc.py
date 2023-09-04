# Import the random library from python module
from random import randint

def play_game():
    #generate role with array
    roles = ["Bear", "Ninja", "Cowboy"]
    #WIN LOS INPUT
    win = "You win!"
    los = "You lose!"
    # Generate a random number to pick a random element from the array
    computer = roles[randint(0,2)]#Bear=0,Ninja=1,Cowboy=2, numbers assigned in roles array
    player = False

    while player == False:
        #prompt player role/input
        player = input("Bear, Ninja, or Cowboy? > ")


    #create logic to check if draw
    if computer == player:
        print("DRAW!", player,"hugs", computer)
    # check who wins
    elif computer == "Cowboy":
        if player == "Bear":
            print(los, player, "is shot by", computer)
        else: #computer is cowboy and player is ninja
            print(win, player, "minces", computer)
    elif computer == "Bear":
        if player == "Cowboy":
            print(win, player, "shoots", computer)
        else: #comp is bear, player is ninja
            print(los, player, "is eaten by", computer)
    elif computer == "Ninja":
        if player == "Cowboy":
            print(los, player, "is minced by", computer)
        else: #computer is ninja player is bear
            print(win, player, "eats", computer)

    #play again?
    play_again = input("Would you like to play again? (yes/no) > ")
    while play_again == 'no':
       break
    #game loop, set player to false and restart the game over and over
    #player = False #clear player input?
    #computer = roles[randint(0,2)]
play_game()