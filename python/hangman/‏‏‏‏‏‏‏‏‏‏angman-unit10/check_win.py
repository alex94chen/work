#7.3.2
def check_win(secret_word, old_letters_guessed):
    """Checks if the whole secret word was guessted correctly
   	:param: secret_word: the word to be guessed
    :param: old_lettes_guessed: the letters that were guessted (user's input)
    :type secret_word: list
    :type old_lettes_guessed: list
    :return: True if the secret word was guessed, False if not
    :rtype: boolean
    """
   
    for i in secret_word:
        if i not in old_letters_guessed:
            return False
    return True