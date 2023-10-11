def check_winner(board, k):
    for i in range(k):
        if all(cell == "X" for cell in board[i]) or all(cell == "O" for cell in board[i]):
            return board[i][0]
        if all(row[i] == "X" for row in board) or all(row[i] == "O" for row in board):
            return board[0][i]

    if all(board[i][i] == "X" for i in range(k)) or all(board[i][i] == "O" for i in range(k)):
        return board[0][0]
    if all(board[i][k - 1 - i] == "X" for i in range(k)) or all(board[i][k - 1 - i] == "O" for i in range(k)):
        return board[0][k - 1]

    return "Ничья"


board = []
k = 3  #Код работает только для поля 3х3

for _ in range(k):
    row = input().strip()
    board.append(list(row))

winner = check_winner(board, k)

print(winner)
