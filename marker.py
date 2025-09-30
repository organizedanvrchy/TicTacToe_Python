import time

# Getting Player Marker Choice (X or O)
def get_player_markers():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1 (Choose X or O): ").upper()
        if marker != 'X' and marker != 'O':
            print("Invalid Choice. Please Enter X or O.\n")
            time.sleep(1)

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
# Updating Game Board With Player Input
def set_player_marker(board, marker, position):
    board[position] = marker
