def is_valid_input(letter_guessed):
    """Checks the validation of input (character)
    :param: letter_guessed
    :type: string
    :return: Whether or not the input was valid
    :rtype: boolean
    """
    return (len(letter_guessed) == 1) and (letter_guessed.isalpha())
    
