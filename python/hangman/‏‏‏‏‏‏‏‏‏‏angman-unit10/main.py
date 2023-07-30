from const import MAX_TRIES, HANGMAN_ASCII_ART, HANGMAN_PHOTOS
from check_valid_input import check_valid_input
from check_win import check_win
from choose_word import choose_word
from show_hidden_word import show_hidden_word
from try_update_letter_guessed import try_update_letter_guessed

    
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
        print(f"letter_guessed: {letter_guessed.encode('ascii')}")
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
