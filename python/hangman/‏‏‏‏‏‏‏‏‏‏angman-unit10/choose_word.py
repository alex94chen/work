#9.4.1
import pytest
import os
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
    if not isinstance(file_path, str) or not isinstance(index, int):
        raise TypeError("file_path must be a string and index must be an integer.")
    
    if not file_path:
        raise ValueError("File name cannot be an empty string.")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' does not exist.")
        
    with open(file_path, 'r') as file:
        file_string = file.read()
        
    file_list = file_string.split(" ")
    word_index = file_list[index % len(file_list)-1]
    set_file = set(file_list)
    sum_word = len(set_file)
    
    return word_index    
  