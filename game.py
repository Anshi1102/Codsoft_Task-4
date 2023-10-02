# import random module
import random
# print multiline instruction performstring concatenation of string
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
	+ "Rock vs Paper -> Paper wins \n"
	+ "Rock vs Scissors -> Rock wins \n"
	+ "Paper vs Scissors -> Scissor wins \n")
while True:
    options = ["Rock", "Paper", "Scissors"]
    user_choice = input("Choose Rock, Paper, or Scissors: ")
    computer_choice = random.choice(options)
    print("User's choice: ", user_choice)
    print("Computer's choice: ", computer_choice)
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("User wins!")
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("User wins!")
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("User wins!")
    else:
        print("User loses!")
    st = input("Do you want to play more(y/n):")
    if st == 'n' or st == 'N':
        break
