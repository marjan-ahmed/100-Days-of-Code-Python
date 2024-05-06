import random as rd

while True:
    print("\t Welcome to Rock, Paper, Scissors!")
    print("Enter 1 for rock, 2 for paper, 3 for scissors, or 4 to quit.")
    print('\n')
    player = int(input("Your choice (in number): "))

    if player == 1:
        print("You choose: rock")

    elif player == 2:
        print("You choose: paper")

    elif player == 3:
        print("You choose: scissors")

    elif player == 4:
        print("Quit")
        break

    else:
        raise ValueError("Invalid input. Try again.")
        continue

    comp = rd.randint(1,3)

    if comp == 1:
        print("Computer choose: rock")

    elif comp == 2:
        print("Computer choose: paper")

    elif comp == 3:
        print("Computer choose: scissors")

    else:
        print("Invalid input. Try again.")
        continue

    def tie():
        if player == comp:
            print("It's a tie! \n")

    def winner():
        if player == 1 and comp == 3 or player == 2 and comp == 1 or player == 3 and comp == 2:
            print("You Win!!! \n")  # 1 for rock | 2 for paper | 3 for scissor

    def lose():
        if player == 1 and comp == 2 or player == 2 and comp == 3 or player == 3 and comp == 1:
            print("You Lose!!! \n")  # 1 for rock | 2 for paper | 3 for scissor
    tie()
    winner()
    lose()