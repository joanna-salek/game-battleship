from random import randint


class Ship:
    def __init__(self, size, orientation):
        self.size = size
        self.orientation = "vertical" if orientation == 0 else "horizontal"
        self.__set_random_localization()

    def __set_random_localization(self):
        self.row = []
        self.col = []
        start = randint(1, 9 - self.size)
        stop = start + self.size - 1
        if self.orientation == "vertical":
            self.col.append(randint(1, 9))
            for i in range(start, stop + 1):
                self.row.append(i)
        else:
            self.row.append(randint(1, 9))
            for i in range(start, stop + 1):
                self.col.append(i)

    def __repr__(self):
        return 'Ship(size=' + str(self.size) + ', orientation=' + self.orientation + ', row= ' + str(self.row) + ', col= ' + str(self.col) + ')'

    def __str__(self):
        return 'Ship(size=' + str(self.size) + ', orientation=' + self.orientation + ', row= ' + str(self.row) + ', col= ' + str(self.col) + ')'


class ShipContainer:
    def __init__(self):
        self.ships = []

    def addShip(self, ship):
        self.ships.append(ship)


ship1 = Ship(2, randint(0, 1))
ship2 = Ship(4, randint(0, 1))

shipContainer = ShipContainer()
shipContainer.addShip(ship1)
shipContainer.addShip(ship2)


print(shipContainer.ships)


class Board():
    def __init__(self):
        self.board = []
        self.create_board()

    def create_board(self):
        for x in range(0, 9):
            self.board.append(["0"] * 9)

    def ships_on_board(self):
        for ship in shipContainer.ships:
            if ship.orientation == "vertical":
                for row in ship.row:
                    col = ship.col[0]
                    self.board[row - 1][col - 1] = "Y"
            elif ship.orientation == "horizontal":
                for col in ship.col:
                    row = ship.row[0]
                    self.board[row - 1][col - 1] = "Y"

    def game(self, x, y):
        if 1 <= x <= 9 and 1 <= y <= 9:
            if self.board[x - 1][y - 1] == "Y":
                print("You've got one")
                self.board[x - 1][y - 1] = "W"
            elif self.board[x - 1][y - 1] == "W":
                print("You've already got this one")
            elif self.board[x - 1][y - 1] == "0":
                print("You've missed this time")
                self.board[x - 1][y - 1] = "X"
            elif self.board[x - 1][y - 1] == "X":
                print("You've already tried this one")
        else:
            print("You are out of a sea, try again")

    def if_ships_left(self):
        hidden_ships = [i for sublist in self.board for i in sublist]
        if "Y" in hidden_ships:
            return True
        else:
            return False

    def show_board(self):
        for row in self.board:
            print(str(" ".join(row)))


board = Board()
gamer_board = Board()
board.ships_on_board()



def main():
    turn = 1
    print ("\nWhere the shipps are located? \nGuess row and column in range from 1 to 9, you only have 15 tries")
    while board.if_ships_left():
        if turn < 16:
            print("Turn {}".format(turn))
            turn += 1
            while True:
                try:
                    guess_row = int(input("Guess row: "))
                    guess_col = int(input("Guess column: "))
                    break
                except ValueError:
                    print("Oops, It wasn't valid number, try again")
            board.game(guess_row, guess_col)
            for i in range(len(board.board)):
                for j in range(len(board.board[0])):
                    if board.board[i][j] in "W, X":
                        gamer_board.board[i][j] = board.board[i][j]

            gamer_board.show_board()
            print("\n")
        else:
            print("Game over")
            break
    else:
        print("Congratulations, you win!")


main()
