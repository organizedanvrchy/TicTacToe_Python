import os

# Clearing The Screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
