import random
import pickle

#import os
# os.system("clear")

buildinglist = ["R", "I", "C", "O", "*"]
alpha = "ABCDEFGHIJKLMNOPQRST"


class Map(object):
    def __init__(self):
        self.buildings = []
        self.buildingStatus = None
        self.score = 0

        self.turn = 0
        self.coinNo = 16

    def createMap(self):
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

            if (len(self.buildings) == 0):
                for j in range(20):
                    print("|", end="     ")
            else:
                for j in range(20):

                    self.buildingStatus = False

                    for building in self.buildings:
                        if ((building.column) == j and building.row == i):
                            print("|  {}  ". format(building.Name), end="")
                            self.buildingStatus = True

                    if self.buildingStatus == False:
                        print("|", end="     ")

            print("|")

        print("", end="    ")
        for j in range(20):
            # Display
            print("+-----", end="")
        print("+\n")

    def addBuilding(self, building):
        self.buildings.append(building)

        self.turn -= 1
        self.coinNo -= 1

    def checkPlacement(self, build):
        hasAdjbuild = False
        for building in self.buildings: 
            if building == build:
                hasAdjbuild = False
            elif (building.column == build.column):
                if (build.row == building.row + 1) or (build.row + 1 == building.row):
                    hasAdjbuild = True
            elif (building.row == build.row):
                if (build.column == building.column + 1) or (build.column + 1 == building.column):
                    hasAdjbuild = True

        return hasAdjbuild


class Building():
    def __init__(self, Name, row, column):
        self.Name = Name
        self.row = row
        self.column = column


def MainMenu():
    print("\nWelcome, mayor of Ngee Ann City")
    print("-------------------------------")
    print("1. Start new game")
    print("2. Load saved game")
    print("3. High Scores")
    print()
    print("0. Exit game")

    # Prompt user to input choice
    # Get choice
    choice = input("\nYour choice: ")
    return choice


def run():
    game = Map()
    choice = MainMenu()

    while True:
        if choice == "1":
            while game.turn <= 400 or game.coinNo != 0:
                game.createMap()
                # set randombuilding1=random.randint(0,4) to get random numbers
                randombuilding1 = buildinglist[random.randint(0, 4)]
                # set randombuilding2=random.randint(0,4) to get random numbers
                randombuilding2 = buildinglist[random.randint(0, 4)]

                while randombuilding1 == randombuilding2:
                    randombuilding2 = random.randint(0, 4)

                print("No. of coins:" + str(game.coinNo))
                print("1. Build {}".format(randombuilding1))
                print("2. Build {}".format(randombuilding2))
                print()
                print("3. Save game")
                print("4. Check Score")
                print("0. Main Menu\n")
                buildingChoice = input("Enter your choice: ")

                if buildingChoice == "1":
                    tobeBuilt = randombuilding1

                elif buildingChoice == "2":
                    tobeBuilt = randombuilding2

                elif buildingChoice == "3":
                    pickle.dump(game, open("buildings.dat", "wb"))
                    break

                elif buildingChoice == "0":
                    print("--------------------------------")
                    choice = MainMenu()
                    game.buildings = []
                    continue

                else:
                    print("Please enter a valid option :)")
                    continue

                Placement = input("Enter your placement: ")

                #validation for placement
                while len(Placement) != 2 or Placement[0].isalpha == False or Placement[1].isnumeric == False:
                    print("Invalid placement. Please try again.")
                    Placement = input("Enter your placement: ")

                for i in range(20):
                    if Placement[0].upper() == alpha[i]:
                        column = i

                row = int(Placement[1:])-1

                build = Building(tobeBuilt, row, column)

                if len(game.buildings) == 0:
                    game.addBuilding(build)

                elif len(game.buildings) != 0:
                    adjbuilding = game.checkPlacement(build)
                    while adjbuilding == False:
                        print("Invalid placement. Please try again.")
                        Placement = input("Enter your placement: ")
                        #validation for placement
                        while len(Placement) != 2 or Placement[0].isalpha == False or Placement[1].isnumeric == False:
                            print("Invalid placement. Please try again.")
                            Placement = input("Enter your placement: ")
                        for i in range(20):
                            if Placement[0].upper() == alpha[i]:
                                column = i

                        row = int(Placement[1:])-1

                        build = Building(tobeBuilt, row, column) 
                        adjbuilding = game.checkPlacement(build) 
                    else:
                        game.addBuilding(build)
                    continue

                continue

        elif choice == "2":
            game = pickle.load(open("buildings.dat", "rb"))
            choice = "1"
            print()
            continue

        elif choice == "0":
            print("\nThank you for playing!")
            print("--------------------------------")
            break

        else:
            print("\nInvalid option")
            choice = MainMenu()
            continue


if __name__ == "__main__":
    run()
