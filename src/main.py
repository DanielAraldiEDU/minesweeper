import random

class Minesweeper:
    def __init__(self, width: int, height: int, bombsQuantity: int) -> None:
        self.width = width
        self.height = height
        self.bombsQuantity = bombsQuantity
        self.campo = [['-' for _ in range(height)] for _ in range(width)]
        self.bombs = set()
        self.is_showed = set()
        self.create_bombs()
        self.count_bombs_around_of_cells()

    def create_bombs(self) -> None:
        while len(self.bombs) < self.bombsQuantity:
            width: int = random.randint(0, self.width - 1)
            height: int = random.randint(0, self.height - 1)
            self.bombs.add((width, height))

    def count_bombs_around_of_cells(self) -> None:
        self.adjacent = [[0 for _ in range(self.height)]
                         for _ in range(self.width)]
        for x, y in self.bombs:
            for i in range(max(0, x - 1), min(self.width, x + 2)):
                for j in range(max(0, y - 1), min(self.height, y + 2)):
                    if (i, j) not in self.bombs:
                        self.adjacent[i][j] += 1

    def print_showed_field(self) -> None:
        for i in range(self.width):
            row = []
            for j in range(self.height):
                if (i, j) in self.is_showed:
                    row.append(
                        str(self.adjacent[i][j]) if (
                            i, j) not in self.bombs else 'B')
                else:
                    row.append('-')
            print(" ".join(row))
        print("\n")

    def show_selected_field(self, x: int, y: int) -> bool:
        if (x, y) in self.bombs:
            print(f"You dead to bomb in {x}, {y} coordinates! End game!")
            self.is_showed.update(self.bombs)
            return True
        else:
            self.is_showed.add((x, y))
            return False

    def is_winner(self) -> bool:
        return len(
            self.is_showed) == self.width * self.height - self.bombsQuantity

def validate_input(message: str, minimum: int, maximum: int) -> int:
    while True:
        try:
            value: int = int(input(message))
            if minimum <= value <= maximum:
                return value
            else:
                print(
                    f"Please, enter a value between {minimum} and {maximum}.")
        except ValueError:
            print("Invalid value. Please, enter an integer value.")

def init() -> None:
    width: int = validate_input("Enter the width of the field: ", 3, 25)
    height: int = validate_input("Enter the height of the field: ", 3, 25)
    bombsQuantity: int = validate_input("Enter the number of bombs: ", 1, 25)

    game: Minesweeper = Minesweeper(width, height, bombsQuantity)
    is_end: bool = False

    while not is_end:
        game.print_showed_field()
        x: int = validate_input(
            f"Enter the width coordinate (0 until {width - 1}): ", 0,
            width - 1)
        y: int = validate_input(
            f"Digite the height coordinate (0 until {height - 1}): ", 0,
            height - 1)

        is_end = game.show_selected_field(x, y)

        if game.is_winner():
            print("Congrats! You won!!!")
            is_end = True

    game.print_showed_field()
    print("Eng game!")

init()
