"""
The game() function is a program let's user play a game and returns the score as an integer.
You need to read a file 'Hi-score.text' which is either blank or contains the previous Hi-score.
You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

"""
import random

def game():
    print("You are playing.... ")
    score = random.randint(0,70)
    # fetch the high score
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
        if(hiscore!= ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your hi-score is : {score}")
    print(f"Previous high score was: {hiscore}")
    if(score>hiscore):
        # write the high score
        print("🎉 New High Score!")
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    return score

game()