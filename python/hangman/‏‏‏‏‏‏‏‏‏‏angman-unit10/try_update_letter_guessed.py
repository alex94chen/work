from check_valid_input import *

#6.4.2
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Checks the validation of input (character) refers to the letters that the player has already guessed in the game.
    :param letter_guessed:The string representing a character inputted by the player.
    :param old_letters_guessed: A list containing the characters entered by the player.  
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: Whether or not the input was valid
    :rtype: boolean
    """
    letter_guessed = letter_guessed.lower()
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    
    else:
        old_letters_guessed.sort(key=str.lower)
        print("X\n" + " -> ".join(old_letters_guessed))
        return False    