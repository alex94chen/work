#import files
import pytest
from main import main
from const import MAX_TRIES, HANGMAN_ASCII_ART, HANGMAN_PHOTOS
from check_valid_input import check_valid_input
from check_win import check_win
from choose_word import choose_word
from show_hidden_word import show_hidden_word
from try_update_letter_guessed import try_update_letter_guessed

# Test cases for the show_hidden_word function
def test_show_hidden_word():
    assert show_hidden_word("python", ["p", "y", "t", "h"]) == "p y t h _ _"
    assert show_hidden_word("hangman", ["h", "a", "n"]) == "h a n _ _ a n"
    assert show_hidden_word("ab", ["c", "g"]) == "_ _"
    assert show_hidden_word("3d", ["a", "f"]) == "_ _"
    assert show_hidden_word("", [""]) == ""
    assert show_hidden_word("b", ["a", "h",  "n","p",  "s" , "y"]) == "_"

# Test cases for the check_valid_input function
def test_check_valid_input():
    assert check_valid_input("3", [])== False
    assert check_valid_input("as", [])== False
    assert check_valid_input("&", [])== False
    assert check_valid_input("a", ["a"])== False
    assert check_valid_input("b", ["a"])== True
       
# Test cases for the check_win function
def test_check_win():
    assert check_win("hello", ["h", "e", "l"]) == False
    assert check_win("python", ["a", "p", "y", "t", "h"]) == False
    assert check_win("hello", ["h", "e", "l", "o", "s"]) == True
    assert check_win("python", ["p", "y", "t", "h", "o", "n"]) == True    

# Test cases for the test_choose_word_empty_string function
def test_choose_word_empty_string():
    with pytest.raises(ValueError) as e:
        choose_word("", 3)
    assert str(e.value) == "File name cannot be an empty string."
        
# Test cases for the test_choose_word_with_number function
def test_choose_word_with_number():
    with pytest.raises(Exception):
        choose_word(3, 3)

# Test cases for the test_choose_word_with_str function
def test_choose_word_with_str():
    with pytest.raises(TypeError):
        choose_word("words.txt", "a")

# Test cases for the test_choose_word_with_path function
def test_choose_word_with_path():  
    with pytest.raises(Exception):
        choose_word("\\%", 3)

# Test cases for the test_choose_word function
def test_choose_word():        
    assert choose_word("words.txt", 3) == "most"

# Test cases for the try_update_letter_guessed function
def test_try_update_letter_guessed():
    assert try_update_letter_guessed("a", ["a"]) == False
    assert try_update_letter_guessed("4", ["a"]) == False
    assert try_update_letter_guessed("%", ["a"]) == False
    assert try_update_letter_guessed("af", ["a"]) == False
    assert try_update_letter_guessed("B", ["a"]) == True
    assert try_update_letter_guessed("h", ["a"]) == True
