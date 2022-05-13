print("Welcome to the Quiz game!")

question = input("Do you want to play the Quiz? \n")

if question.lower() != "yes":
    quit()
else:
    print("Okay, Let's play the game.")

def quiz(answer,guess):
    global score
    
    if answer.lower().strip() == guess:
       print("Correct!") 
       score += 1
      
    else:
        print("Incorrect!")

score = 0
answer1 = input("What is the smallest planet in our solar system? \n")
guess1 = "mercury"
quiz(answer1,guess1)

answer2 = input("What has one eye but can't see? \n")
guess2 = "needle"
quiz(answer2,guess2)

answer3 = input("What can run but cannot walk? \n")
guess3 = "river"
quiz(answer3,guess3)

answer4 = input("What kind of room has no doors or windows? \n")
guess4 = "mushroom"
quiz(answer4,guess4)

answer5 = input("What type of dress can never be worn? \n")
guess5 = "address"
quiz(answer5,guess5)


print(f"Your total score is {score}")





