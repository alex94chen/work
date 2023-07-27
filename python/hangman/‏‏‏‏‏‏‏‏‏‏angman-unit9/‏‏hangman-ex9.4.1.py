def choose_word(file_path, index):
    """
    Choose a word from a file based on the specified index and count the number of unique words in the file.

    :param file_path: The path to the file.
    :type file_path: str
    :param index: The index of the word to choose.
    :type index: int
    :return: A tuple containing the number of unique words and the word at the specified index.
    :rtype: tuple
    """
    
    with open(file_path, 'r') as file:
        file_string = file.read()
        
    file_list = file_string.split(" ")
    word_index = file_list[index % len(file_list)-1]
    set_file = set(file_list)
    sum_word = len(set_file)
    
    return (sum_word, word_index)



file_path = r"C:\work\python\files\words.txt"
index = 15
print(f"choose_word(file_path, index): {choose_word(file_path, index)}")

