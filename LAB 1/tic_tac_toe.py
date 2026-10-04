board = [[-1, -1, -1],
         [-1, -1, -1],
         [-1, -1, -1]]

game = int(input("Enter 0 for Bot vs Bot, 1 for Human vs Bot: "))

boards = []


def evaluate(board, pawn):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == pawn:
            return 1

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == pawn:
            return 1

    if board[0][0] == board[1][1] == board[2][2] == pawn:
        return 1

    if board[0][2] == board[1][1] == board[2][0] == pawn:
        return 1

    return 0


def move(board, pawn):
    enemy = 1 - pawn

    for r in range(3):
        for c in range(3):
            if board[r][c] == -1:
                board[r][c] = pawn

                if evaluate(board, pawn):
                    return

                board[r][c] = -1

    for r in range(3):
        for c in range(3):
            if board[r][c] == -1:
                board[r][c] = enemy

                if evaluate(board, enemy):
                    board[r][c] = pawn
                    return

                board[r][c] = -1

    if board[1][1] == -1:
        board[1][1] = pawn
        return

    for r in range(3):
        for c in range(3):
            if board[r][c] == -1:
                board[r][c] = pawn
                return


def print_board(board):
    print()

    for r in range(3):
        print(" | ".join(
            "." if board[r][c] == -1 else str(board[r][c])
            for c in range(3)
        ))

        if r < 2:
            print("--+---+--")

    print()


def print_boards(boards):
    for i in range(0, len(boards), 5):
        group = boards[i:i + 5]

        for r in range(3):
            lines = []

            for board in group:
                lines.append(" | ".join(
                    "." if board[r][c] == -1 else str(board[r][c])
                    for c in range(3)
                ))

            print("     ".join(lines))

            if r < 2:
                print("     ".join(["--+---+--"] * len(group)))

        print()


def check_winner(board, pawn):
    return evaluate(board, pawn) == 1


def board_full(board):
    for row in board:
        for cell in row:
            if cell == -1:
                return False

    return True


turn = 0

while turn < 9:

    if game == 0:

        pawn = turn % 2
        move(board, pawn)

    else:

        if turn % 2 == 0:

            while True:
                r = int(input("Enter row (0-2): "))
                c = int(input("Enter column (0-2): "))

                if r < 0 or r > 2 or c < 0 or c > 2:
                    print("Invalid position!")
                    continue

                if board[r][c] != -1:
                    print("Invalid move!")
                    continue

                board[r][c] = 0
                break

        else:

            move(board, 1)

            print("Bot moved:")
            print_board(board)

    boards.append([row[:] for row in board])

    if check_winner(board, 0):
        break

    if check_winner(board, 1):
        break

    if board_full(board):
        break

    turn += 1


if game == 0:
    print_boards(boards)

if check_winner(board, 0):
    print("0 wins!")

elif check_winner(board, 1):
    print("1 wins!")

else:
    print("Draw!")
