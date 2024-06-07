import time

# Mulai hitung waktu
start_time = time.time()

# Fungsi untuk menampilkan papan permainan
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Fungsi untuk memeriksa apakah papan permainan penuh
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Fungsi untuk memeriksa apakah langkah tertentu menghasilkan kemenangan
def is_winner(board, player):
    # Mengecek baris dan kolom
    for i in range(3):
        if board[i] == [player, player, player] or [row[i] for row in board] == [player, player, player]:
            return True

    # Mengecek diagonal
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Fungsi untuk mendapatkan semua langkah yang tersedia
def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves

# Fungsi untuk melakukan langkah pemain
def player_move(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))
            if board[row][col] != " ":
                print("Invalid move. Try again.")
            else:
                board[row][col] = player
                break
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")

# Fungsi untuk melakukan langkah komputer menggunakan algoritma backtracking
def computer_move(board, player):
    best_move = None
    best_score = float("-inf")
    available_moves = get_available_moves(board)

    for move in available_moves:
        board[move[0]][move[1]] = player
        score = minimax(board, 0, False)
        board[move[0]][move[1]] = " "
        if score > best_score:
            best_score = score
            best_move = move

    if best_move:
        board[best_move[0]][best_move[1]] = player

# Fungsi rekursif untuk algoritma minimax dengan cost
def minimax(board, depth, is_maximizing):
    if is_winner(board, "X"):
        return -10 ** (len(get_available_moves(board)) + 1)
    if is_winner(board, "O"):
        return 10 ** (len(get_available_moves(board)) + 1)
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# Fungsi utama permainan Tic-Tac-Toe
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not is_board_full(board) and not is_winner(board, "X") and not is_winner(board, "O"):
        # Giliran pemain X
        player_move(board, "X")
        print_board(board)

        # Periksa kondisi setelah langkah pemain X
        if is_winner(board, "X"):
            print("Player X wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        # Giliran pemain O
        computer_move(board, "O")
        print_board(board)

        # Periksa kondisi setelah langkah pemain O
        if is_winner(board, "O"):
            print("Player O wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

# Memulai permainan
play_game()

# Akhiri hitung waktu
end_time = time.time()

# Hitung waktu eksekusi
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
