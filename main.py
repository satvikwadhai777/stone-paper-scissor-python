import random

# Stone Paper Scissor Game

choices = {
    "s": "Stone",
    "p": "Paper",
    "sc": "Scissor"
}

computer = random.choice(["s", "p", "sc"])

user = input("Enter your choice (s for Stone, p for Paper, sc for Scissor): ").lower()

if user not in choices:
    print("Invalid choice! Please enter s, p, or sc.")
else:
    print("You chose:", choices[user])
    print("Computer chose:", choices[computer])

    if user == computer:
        print("It's a Draw!")

    elif user == "s" and computer == "sc":
        print("You Win! Stone breaks Scissor.")

    elif user == "p" and computer == "s":
        print("You Win! Paper covers Stone.")

    elif user == "sc" and computer == "p":
        print("You Win! Scissor cuts Paper.")

    else:
        print("You Lose! Computer wins.")
