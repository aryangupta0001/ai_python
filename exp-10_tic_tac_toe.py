# Tic Tac Toe Game in Python
# Display the board
def display_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check if there's a winner

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([cell == player for cell in row]):
            return True
    
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
        if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):    
            return True
        return False

# Check if the board is full
def check_full(board):
    return all([cell != " " for row in board for cell in row])

# Main game function
def play_game():
    # Initialize the game board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    # Main game loop

    while True:
        display_board(board)
        print(f"Player {current_player}'s turn")
        
        # Get player move
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if board[row][col] != " ":
                print("Cell is already taken! Choose another.")
                continue

        except (ValueError, IndexError):
            print("Invalid input! Please enter numbers between 1 and 3.")
            continue
        
        # Update the board with the current player's move
        board[row][col] = current_player
        
        # Check for a winner
        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a tie
        if check_full(board):
            display_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"
        203
# Run the game
play_game()