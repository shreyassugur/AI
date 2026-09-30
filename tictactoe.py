import math
board = [" " for _ in range(9)]

def show():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def win(player):
    lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
             [0, 3, 6], [1, 4, 7], [2, 5, 8],
             [0, 4, 8], [2, 4, 6]]
    for line in lines:
        if all(board[i] == player for i in line):
            return True
    return False

def full():
    return " " not in board

def minimax(is_ai):
    if win("O"):
        return 1
    if win("X"):
        return -1
    if full():
        return 0
    if is_ai:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)
        return best

def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

print("Tic-Tac-Toe")
print("You are X")
print("Enter numbers from 1 to 9")

while True:
    show()
    try:
        choice = int(input("Your move: ")) - 1
    except ValueError:
        print("Please enter a number from 1 to 9.")
        continue

    if 0 <= choice < 9 and board[choice] == " ":
        board[choice] = "X"
    else:
        print("Invalid move")
        continue

    if win("X"):
        show()
        print("You win!")
        break

    if full():
        show()
        print("Draw!")
        break

    ai_move()

    if win("O"):
        show()
        print("Computer wins!")
        break

    if full():
        show()
        print("Draw!")
        break
11