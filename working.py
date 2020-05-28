board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def board_printing_func(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def check_valid(board, number, position):

    for i in range(len(board[0])):
        if board[position[0][i]] == number and position[1] != i:
            return False

    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    x_box = position[1] // 3
    y_box = position[0] // 3

    for i in range(y_box*3, y_box*3 + 3):
        for j in range(x_box*3, x_box*3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False

    return True

def empty_finder(bo):
	for i in range(len(bo)):
		for j in range(len(bo[0])):
			if bo[i][j] == 0:
				return (i , j)