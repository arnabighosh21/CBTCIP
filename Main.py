import random

print(".........Welcome to Rock-Paper-Scissors-Game......")

user_score = 0
comp_score = 0
ties = 0

name = input("Enter your name here :")
print("""
winning rules:
1.Paper vs Rock --> Paper
2.Rock vs Scissors --> Rock
3. Scissors vs Paper --> Scissors """)

while True:
    print("""choice are:
    1.Rock
    2.paper
    3. Scissors""")
    choice = int(input("enter your choice from  1-3 : "))
    print()
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input"))
    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "paper"
    else:
        user_choice = "Scissors"
    print("The user's choice is", user_choice)
    print("now it is Computer's turn")

    computer = random.randint(1, 3)

    if computer == 1:
        comp_choice = "Rock"
    elif computer == 2:
        comp_choice = "paper"
    else:
        comp_choice = "Scissors"

    print("The computer's choice is", comp_choice)

    if ((user_choice == "paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "paper")):
        print("paper wins")
        result = "paper"
    elif ((user_choice == "Scissors" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Scissors")):
        print("Rock wins")
        result = "Rock"

    elif (user_choice == comp_choice):
        print("it is a tie")
        result = "Tie"

    else:
        print("Scissors wins")
        result = "Scissors"
    if result == "Tie":
        ties += 1
    elif result == user_choice:
        user_score += 1
    else:
        comp_score += 1

    print("Scores are")
    print(name, " ' s score is", user_score)
    print("computer's score is", comp_score)
    print("ties are", ties)

    repeat = input(" do you  want to play again ?")
    if repeat == "No" or repeat == "No":
        break
print("thanks for playing")