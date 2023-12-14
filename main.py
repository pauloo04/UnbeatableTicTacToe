board = [[" " for col in range(3)] for row in range(3)]

ai = "X"
human = "O"

winning_lines = [[[0,0],[1,1],[2,2]],[[0,2],[1,1],[2,0]],
                 [[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],
                 [[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]]]

def print_board(table):
    for row in table:
        for el in row:
            print(el, end=" ")
        print()
    print("\n")

def win_check():
    for line in winning_lines:
        if (board[line[0][0]][line[0][1]] == board[line[1][0]][line[1][1]] == board[line[2][0]][line[2][1]]) and board[line[0][0]][line[0][1]] != " ":
            return board[line[0][0]][line[0][1]]
    if (" " not in board[0]) and (" " not in board[1]) and (" " not in board[2]):
        return "tie"
    return None

def bestMove():
    bestScore = -1000000
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = ai
                score = minimax(board, False)
                board[i][j] = " "
                if score > bestScore:
                    bestScore = score
                    move = [i,j]
    return move

scores = {
    "X": 1,
    "O": -1,
    "tie": 0
}

def minimax(board, isMaximizing):
    result = win_check()
    if result != None:
        return scores[result]
    if isMaximizing:
        bestScore = -1000000
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = ai
                    score = minimax(board, False)
                    board[i][j] = " "
                    bestScore = max(bestScore, score)
        return bestScore
    else:
        bestScore = 1000000
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = human
                    score = minimax(board, True)
                    board[i][j] = " "
                    bestScore = min(bestScore, score)
        return bestScore

def game():
    curr_player = ai
    winner = win_check()
    while not winner:
        if curr_player == ai:
            move = bestMove()
            board[move[0]][move[1]] = curr_player
            curr_player = human
            print(f"Computer makes move {move[0]} {move[1]}")
        else:
            valid_move_made = False
            while not valid_move_made:
                move = input("Enter your move: ")
                if board[int(move.split()[0])][int(move.split()[1])] == " ":
                    board[int(move.split()[0])][int(move.split()[1])] = curr_player
                    curr_player = ai
                    valid_move_made = True
                else:
                    print("Invalid move! The square has already been taken!")
        print_board(board)
        winner = win_check()
    match scores[winner]:
        case 1:
            print("Computer wins!")
        case 0:
            print("It's a tie!")
        case -1:
            print("You win!")

if __name__ == "__main__":
    game()
