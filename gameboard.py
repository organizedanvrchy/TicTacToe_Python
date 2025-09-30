# Displaying Information
def display_gameboard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

# Checking If Position Is Available
def is_position_available(board, position):
    if board[position] == ' ':
        return True
    else:
        print("Position Is Taken. Please Try Again...")

# Checking If Board Is Full
def is_board_full(board):
    for space in board:
        if space == ' ': 
            return False  # Board Is Not Full
    return True

# Getting Position Player Wants To Place Marker
def player_choice(board, turn):
    position = None
    while True:
        try:
            position = int(input(f"\n{turn} Please Enter A Position (1 - 9): ")) - 1
            if position not in range(9):
                print("Invalid input! Please enter a number between 1 and 9.")
            elif not is_position_available(board, position):
                print("Position is taken. Please try again...")
            else:
                return position
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")
    
# Checking For Win State
def get_game_state(board, markers):
    player1_marker, player2_marker = markers

    for marker in markers:
        if (board[0] == board[1] == board[2] == marker or 
            board[3] == board[4] == board[5] == marker or 
            board[6] == board[7] == board[8] == marker or
            board[0] == board[3] == board[6] == marker or
            board[1] == board[4] == board[7] == marker or
            board[2] == board[5] == board[8] == marker or
            board[0] == board[4] == board[8] == marker or
            board[2] == board[4] == board[6] == marker
            ):
            print("\nGAME OVER\n")

            if marker == player1_marker:
                print("\nPlayer 1 Wins!\n")
                display_gameboard(board)
                return True
            elif marker == player2_marker:
                print("\nPlayer 2 Wins!\n")
                display_gameboard(board)
                return True
    
    # Checking For Tie State
    if is_board_full(board):
        print("\nIt's a Tie\n")
        display_gameboard(board)
        return True
    
    return False
