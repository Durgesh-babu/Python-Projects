board = [['1','2','3'],
         ['4','5','6'],
         ['7','8','9']]
p1 = ''
p2 = ''
tie = False
r = 0
c = 0
key = 'X'

def main():
    p1 = input("Enter player 1 name: ")
    p2 = input("Enter player 1 name: ")
    print('-----------------------------------------------------')
    print(f'{p1} plays first and {p2} plays next.')
    print('-----------------------------------------------------')

    while not win():
        display_board()
        position()
        win()

def win():
    ...

def position():
    position_var = 0
    global r,c
    if key == 'X':
        position_var = int(input(f'{p1} enter the positon: '))
    else:
        position_var = int(input(f'{p2} enter the positon: '))
    print(r,c)
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
        print('Invalid position!')
        position()

    if board[r][c] != 'X' and board[r][c] != 'O':
        board[r][c] = key
    else:
        print("Occupied!")
        position()

def display_board():
    print(f"---------")
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
    print(f"---------")

if __name__ == '__main__':
    main()