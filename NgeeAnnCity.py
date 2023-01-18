import random

buildinglist = ["R", "I", "C", "O", "*"]
alpha = "ABCDEFGHIJKLMNOPQRST"


class Map(object):
    def __init__(self):
        self.buildings = []
        self.buildingStatus = None
        self.score = 0

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

    def checkPlacement(self, building):
        for buildings in self.buildings:
            hasAdjbuild = False
            if (buildings.column == building.column):
                if (building.row == buildings.row + 1) or (building.row + 1 == buildings.row):
                    hasAdjbuild = True
            elif (buildings.row == building.row):
                if (building.column == buildings.column + 1) or (building.column + 1 == buildings.column):
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
            TurnNo = 1
            CoinNo = 16
            Score = 0
            while TurnNo <= 400 or CoinNo != 0:
                game.createMap()
                # set randombuilding1=random.randint(0,4) to get random numbers
                randombuilding1 = random.randint(0, 4)
                # set randombuilding2=random.randint(0,4) to get random numbers
                randombuilding2 = random.randint(0, 4)

                if randombuilding1 == randombuilding2:
                    randombuilding2 = random.randint(0, 4)

                print("No. of coins:"+ str(CoinNo))
                print("1. Build {}".format(buildinglist[randombuilding1]))
                print("2. Build {}".format(buildinglist[randombuilding2]))
                print()
                print("3. Save game")
                print("4. Check Score")
                print("0. Main Menu\n")
                buildingChoice = input("Enter your choice: ")

                if buildingChoice == "1":
                    randombuilding = randombuilding1

                elif buildingChoice == "2":
                    randombuilding = randombuilding2

                elif buildingChoice == "3":
                    file = open("Load.txt", "a")
                    file.writeline(str(game.buildings))
                    file.writeline(str(game.buildings))
                    file.close()
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

                for i in range(20):
                    if Placement[0].upper() == alpha[i]:
                        column = i

                row = int(Placement[1:])-1

                building = Building(buildinglist[randombuilding], row, column)

                if len(game.buildings) == 0:
                    game.addBuilding(building)

                elif game.checkPlacement(building):
                    game.addBuilding(building)
                    continue

                else:
                    print("try other place.")
                    continue

                continue

        elif choice == "2":
            file = open("Load.txt", "r")
            buildings = file.readlines()
            print(buildings)

            print(buildings)

            file.close()
            choice = "1"
            continue

        elif choice == "0":
            print("\nThank you for playing!")
            print("--------------------------------")

            exit()

        else:
            print("\nInvalid option")
            choice = MainMenu()
            continue


if __name__ == "__main__":
    run()
