import random


def rps():
    choices = ["Rock", "Paper", "Scissors"]

    while(True):
            user_choice = int(input("\nEnter your choice:\n 0 for Rock\n 1 for Paper\n 2 for Scissors\n 3 to Exit the game\nYour choice: "))

            if user_choice == 3:
                print("Thanks for playing! Goodbye.")
                break
            elif user_choice < 0 or user_choice > 3:
                print("Invalid choice ...")
                continue
            computer_choice = random.randint(0,2)
            print("Computer chose :")
            print(computer_choice)

            if computer_choice == user_choice:
                print("Its a DRAW !!!")
            elif(user_choice == 0 and computer_choice == 2) or \
                (user_choice == 1 and computer_choice == 0) or \
                (user_choice == 2 and computer_choice == 1):
                print("You WIN !!!")
            elif(user_choice == 3):
                exit()
            else :
                print("You LOSE !!!")

rps()
