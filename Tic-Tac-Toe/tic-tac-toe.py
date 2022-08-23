board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
p1 = ""
p2 = ""
tie = False
r = 0
c = 0
key = "X"


def main():
    global p1, p2, key
    p1 = input("Enter player 1 name: ")
    p2 = input("Enter player 1 name: ")
    print("-----------------------------------------------------")
    print(f"{p1} plays first and {p2} plays next.")
    print("-----------------------------------------------------")

    while not win():
        display_board()
        position()
        win()

    if key == "O" and not tie:
        print(f"{p1} wins!")
    elif key == "X" and not tie:
        print(f"{p2} wins!")
    else:
        print(f"It's a tie!")


def win():
    global tie
    for i in range(3):
        if (board[0][i] == board[1][i] and board[1][i] == board[2][i]) or (
            board[i][0] == board[i][1] and board[i][1] == board[i][2]
        ):
            return True
        if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (
            board[0][2] == board[1][1] and board[1][1] == board[2][0]
        ):
            return True

        for i in range(3):
            for j in range(3):
                if board[i][j] != "X" and board[i][j] != "O":
                    return False

    tie = True
    return True


def position():
    position_var = 0
    global r, c, key
    if key == "X":
        position_var = int(input(f"{p1} enter the positon: "))
    else:
        position_var = int(input(f"{p2} enter the positon: "))
    if position_var == 1:
        r = 0
        c = 0
    elif position_var == 2:
        r = 0
        c = 1
    elif position_var == 3:
        r = 0
        c = 2
    elif position_var == 4:
        r = 1
        c = 0
    elif position_var == 5:
        r = 1
        c = 1
    elif position_var == 6:
        r = 1
        c = 2
    elif position_var == 7:
        r = 2
        c = 0
    elif position_var == 8:
        r = 2
        c = 1
    elif position_var == 9:
        r = 2
        c = 2
    else:
        print("Invalid position!")
        position()

    if board[r][c] != "X" and board[r][c] != "O":
        board[r][c] = key
        if key == "X":
            key = "O"
        else:
            key = "X"
    else:
        print("Occupied!")
        position()


def display_board():
    print(f"---------")
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
    print(f"---------")


if __name__ == "__main__":
    main()
