import const.py

def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks the validation of input (character) refers to the letters that the player has already guessed in the game.
    :param letter_guessed:The string representing a character inputted by the player.
    :param old_letters_guessed: A list containing the characters entered by the player.  
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: Whether or not the input was valid
    :rtype: boolean
    """
    letter_guessed = letter_guessed.lower()
    return (len(letter_guessed) == 1) and (letter_guessed.isalpha()) and (letter_guessed.lower() not in old_letters_guessed)
    
    

def main():
    # Call the function check_valid_input
    old_letters = ['a', 'b', 'c']
    print(check_valid_input('C', old_letters), check_valid_input('ep', old_letters),check_valid_input('$', old_letters) ,check_valid_input('s', old_letters))

if __name__ == "__main__":
    main()
