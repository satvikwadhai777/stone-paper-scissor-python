import random

# Stone Paper Scissor Game

choices = {
    "s": "Stone",
    "p": "Paper",
    "sc": "Scissor"
}

winning_rules = {
    "s": "sc",   # Stone beats Scissor
    "p": "s",    # Paper beats Stone
    "sc": "p"    # Scissor beats Paper
}

while True:
    computer = random.choice(list(choices.keys()))

    user = input("Enter your choice (s for Stone, p for Paper, sc for Scissor): ").lower()

    if user not in choices:
        print("Invalid choice! Please enter s, p, or sc.\n")
        continue

    print("You chose:", choices[user])
    print("Computer chose:", choices[computer])

    if user == computer:
        print("It's a Draw! Match will restart...\n")
        continue

    elif winning_rules[user] == computer:
        print(f"You Win! {choices[user]} beats {choices[computer]}.")
        break

    else:
        print(f"You Lose! {choices[computer]} beats {choices[user]}.")
        break
