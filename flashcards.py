import json
import os

#state directory of file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)    


with open('me-capitals.json', 'r') as f:
    data = json.load(f)

#initialize total as length of cards array
total = len(data["cards"])
# initialize score as 0
score = 0
##endgame message
endgame = "Thanks for playing!"

# add a for loop
for i in data["cards"]:
    guess = input(i["q"] + ">")
# check for correct answer
    if guess == i["a"]:
        # increment score up one
        score += 1
        # interpolate score and total into the response
        print(f"Correct! Current score: {score}/{total}")
    #conditional elif statement
    elif guess.lower() == i["a"].lower():
            score += 1
            #print response
            print(f"Correct! Current score: {score}/{total}")
    else:
            print("Incorrect! The correct answer was", i["a"])
            print (f"Current score: {score}/{total}")
#data["cards"] accesses the value in key-value pairs in a python dic.  

    if score == total:
        print(f"{endgame} You got a perfect score!")
    elif score < total: 
        print("Play again?")