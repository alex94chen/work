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
            
            
       
    

def main():
    # Call the function check_valid_input
    
    secret_word = "friends"
    old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
    print(check_win(secret_word, old_letters_guessed))

    secret_word = "yes"
    old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
    print(check_win(secret_word, old_letters_guessed))



if __name__ == "__main__":
    main()
