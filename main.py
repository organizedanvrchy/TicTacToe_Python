import time
from gameboard import display_gameboard, player_choice, get_game_state
from marker import get_player_markers, set_player_marker
from replay import replay
from utils import clear_screen
from flip import flip

def main():
    print("\n======================")
    print("Welcome to TIC TAC TOE")
    print("======================\n")

    while True:
        default_gameboard = [' '] * 9
        player_markers = get_player_markers()
        player1_marker, player2_marker = player_markers

        print(f"\nPlayer 1: {player1_marker} | Player 2: {player2_marker}\n")

        time.sleep(2)
        clear_screen()

        print("Let's Flip To See Who Goes First!\n")
        print("----------")
        time.sleep(1)
        print("Flipping")
        time.sleep(1)
        print("----------\n")
        time.sleep(1)

        turn = flip()
        if turn == "Player 1":
            print("Player 1 Goes First!\n")
        else:
            print("Player 2 Goes First!\n")

        time.sleep(2)
        clear_screen()

        _is_game_on = True

        while _is_game_on:
            clear_screen()

            if get_game_state(default_gameboard, player_markers):
                _is_game_on = False
                break
            
            print(f"\n{turn}'s turn!\n")

            display_gameboard(default_gameboard)

            position = player_choice(default_gameboard, turn)

            if turn == 'Player 1':
                marker = player1_marker
            else:
                marker = player2_marker

            set_player_marker(default_gameboard, marker, position)

            if turn == 'Player 1':
                turn = 'Player 2'  
            else:
                turn = 'Player 1'
    
        if replay() == 'N':
            break
        else:
            clear_screen()


if __name__ == "__main__":
    main()
    