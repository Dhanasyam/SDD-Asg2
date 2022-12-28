import random


buidingNames = ["R", "I", "C", "O", "*"]
alpha = "ABCDEFGHIJKLMNOPQRST"


def map():
    print("", end="    ")
    for j in range(20):
        print("   {}  ".format(alpha[j]), end="")
    print()

    for i in range(20):
        print("", end="    ")
        for j in range(20):
            # Display
            print("+-----", end="")
        print("+")
        if(i+1 < 10):
            print(i+1, end="   ")

        else:
            print(i+1, end="  ")

        for j in range(20):

            print("|", end="     ")

        print("|")

    print("", end="    ")
    for j in range(20):
        # Display
        print("+-----", end="")
    print("+")


def run():
    while True:
        print("Welcome, mayor of Ngee Ann City")
        print("---------------------------")
        print("1. Start new game")
        print("2. Load saved game")
        print("3. High Scores")
        print()
        print("0. Exit game")

        # Prompt user to input choice
        # Get choice
        choice = input("Your choice? ")

        if choice == "1":
            map()

        if choice == "0":
            break


if __name__ == "__main__":
    run()
