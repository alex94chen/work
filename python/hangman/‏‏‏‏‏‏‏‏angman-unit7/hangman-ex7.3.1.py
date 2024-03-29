def show_hidden_word(secret_word, old_letters_guessed):
    """The function receives a word to guess and the characters that have been guessed so far, 
    and returns the positions of the guessed characters.
    :param secret_word:The string that the player needs to guess
    :param old_letters_guessed: The parameters guessed so far.  
    :type secret_word: string 
    :type old_letters_guessed: list
    :return: The places where guesses have been made so far
    :rtype: string
    """
    secret_word = list(secret_word)
    
    for i in range(len(secret_word)):
        if secret_word[i] not in old_letters_guessed:
            secret_word[i] = '_'
        
    ret_sec = ' '.join(secret_word)
    return ret_sec
            
       
    

def main():
    # Call the function check_valid_input
    
    
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))

    old_letters = ['a', 'b', 'c']
    secret_word = "alex"
    print(show_hidden_word(secret_word, old_letters), show_hidden_word(secret_word, old_letters),show_hidden_word(secret_word, old_letters) ,show_hidden_word(secret_word, old_letters))

if __name__ == "__main__":
    main()
