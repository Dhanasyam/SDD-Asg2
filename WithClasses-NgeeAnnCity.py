import random

buildinglist = ["R", "I", "C", "O", "*"]
alpha = "ABCDEFGHIJKLMNOPQRST"


class Map(object):
    def __init__(self):
        self.buildings = []
        self.currentChoice = 0

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
                    for building in self.buildings:
                        if (building.column == j and building.row == i):
                            print("|  {}  ". format(building.Name), end="")
                        else:
                            print("|", end="     ")
            print("|")

        print("", end="    ")
        for j in range(20):
            # Display
            print("+-----", end="")
        print("+")

    def addBuilding(self, building):
        self.currentChoice = building
        self.buildings.append(self.currentChoice)


class Building():
    def __init__(self, Name, row, column):
        self.Name = Name
        self.row = row
        self.column = column


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
        choice = input("Your choice? \n")

        if choice == "1":
            map = Map()
            map.createMap()

            # set randombuilding1=random.randint(0,4) to get random numbers
            randombuilding1 = random.randint(0, 4)
            # set randombuilding2=random.randint(0,4) to get random numbers
            randombuilding2 = random.randint(0, 4)

            if(randombuilding1 == randombuilding2):
                randombuilding2 = random.randint(0, 4)

            column = 0
            row = 0

            print("1. Builds a {}".format(buildinglist[randombuilding1]))
            print("2. Builds a {}".format(buildinglist[randombuilding2]))
            print()
            buildingChoice = input("Enter your choice?")

            if buildingChoice == "1":
                Placement = input("Enter your placement")

                for i in range(20):
                    if Placement[0].upper() == alpha[i]:
                        column = i

                row = int(Placement[1:])-1

            building = Building(buildinglist[randombuilding1], row, column)
            map.addBuilding(building)
            map.createMap()

        if choice == "0":
            break


if __name__ == "__main__":
    run()
