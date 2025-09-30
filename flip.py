import random

# Flipping for first
def flip():
    coin = random.randint(0, 1)
    if coin == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    