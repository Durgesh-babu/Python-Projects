board = [['1','2','3'],['4','5','6'],['7','8','9']]
p1 = ''
p2 = ''
tie = False
r = 0
c = 0

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
    ...

def display_board():
    print(f"---------")
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
    print(f"---------")

if __name__ == '__main__':
    main()