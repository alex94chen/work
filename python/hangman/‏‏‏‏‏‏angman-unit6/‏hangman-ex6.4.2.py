import const.py

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Checks the validation of input (character) refers to the letters that the player has already guessed in the game.
    :param letter_guessed:The string representing a character inputted by the player.
    :param old_letters_guessed: A list containing the characters entered by the player.  
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: Whether or not the input was valid
    :rtype: boolean
    """
    if (len(letter_guessed) == 1) and (letter_guessed.isalpha()) and (letter_guessed.lower() not in old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    
    else:
        old_letters_guessed.sort(key=str.lower)
        print("X\n" + " -> ".join(old_letters_guessed))
        return False
        

def main():
    # Call the function check_valid_input
    old_letters = ['a', 'p', 'c', 'f']
    print(try_update_letter_guessed('de',['b', 'a', 'c']))

if __name__ == "__main__":
    main()
