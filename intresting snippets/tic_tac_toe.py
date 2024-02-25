# let's play tic tac toe
board = []
for i in range(3):
    row = ["*"] * 3
    board.append(row)

while True:
    row = int(input("which row would you like to fill: ")) - 1 
    element = int(input("which element would you like to fill: ")) - 1

    is_board_empty = board[row][element] == "*"
    if is_board_empty:
        board[row][element] = "X"
        for i in board:
            print(i)
    else:
        print("this cell is already taken")
    
    if board[0][0] == board[1][1] == board[2][2]:
        print("you won the game")
        break
    
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            print("you won the game")
        break