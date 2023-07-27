import sys
sys.const = True

MAX_TRIES = 6

HANGMAN_ASCII_ART ="""Welcome to the game Hangman


      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/ 
                         
"""   
    
HANGMAN_PHOTOS = {
        1: """x-------x
    """,
        2: """
        x-------x
        |
        |
        |
        |
        |
        
    """,
        3: """
        x-------x
        |       |
        |       0
        |
        |
        |

    """,
        4: """
        x-------x
        |       |
        |       0
        |       |
        |
        |
        
    """,
        5: """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
        
    """,
        6: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |

    """,
        7: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
        
    """
    }



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
#7.3.1                
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
#6.4.1
def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks the validation of input (character) refers to the letters that the player has already guessed in the game.
    :param letter_guessed:The string representing a character inputted by the player.
    :param old_letters_guessed: A list containing the characters entered by the player.  
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: Whether or not the input was valid
    :rtype: boolean
    """
    
    return (len(letter_guessed) == 1) and (letter_guessed.isalpha()) and (letter_guessed.lower() not in old_letters_guessed)
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
#9.4.1
def choose_word(file_path, index):
    """
    Choose a word from a file based on the specified index and count the number of unique words.

    :param file_path: The path to the file.
    :type file_path: str
    :param index: The index of the word to choose.
    :type index: int
    :return: A tuple with the number of unique words and the word at the specified index.
    :rtype: tuple

    """

    with open(file_path, 'r') as file:
        file_string = file.read()
        
    file_list = file_string.split(" ")
    word_index = file_list[index % len(file_list)-1]
    set_file = set(file_list)
    sum_word = len(set_file)
    
    return word_index    

    
def main():
    
    print(HANGMAN_ASCII_ART ,MAX_TRIES)    
    
    file_path = input(r"Enter a file path:")
    index = int(input("Enter index:"))
    secret_word = choose_word(file_path, index)   
    
    
    num_of_tries = 1
    
    old_letters_guessed = list()
    print(f"Let’s start!\n{HANGMAN_PHOTOS[num_of_tries]}\n{show_hidden_word(secret_word, old_letters_guessed)}")


    while num_of_tries <= MAX_TRIES:
        
        letter_guessed = input('Guess a letter: ').lower()
        
        if not try_update_letter_guessed(letter_guessed, old_letters_guessed):
            continue
    
        if letter_guessed not in show_hidden_word(secret_word, old_letters_guessed):
            num_of_tries += 1               
            print(f":({(HANGMAN_PHOTOS[num_of_tries])}") 
        
        print(show_hidden_word(secret_word, old_letters_guessed)) 
        
        
        if num_of_tries > MAX_TRIES:
            print("LOSE")
            break
              
        if check_win(secret_word, old_letters_guessed):
            print("WIN")
            break 
            
    
if __name__ == "__main__":
    main()
