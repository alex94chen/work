#9


    



def sort_times(times):
    def convert_time(time):
        minutes, seconds = map(int, time.split(':'))
        return minutes * 60 + seconds
    
    sorted_times = sorted(times, key=convert_time)
    return sorted_times



def find_name(list_name):
    count_dict = {} 

    for name in list_name:
        if name in count_dict:
            count_dict[name] += 1
        else:
            count_dict[name] = 1

    top_name = max(count_dict, key=count_dict.get)
    return top_name    

def my_mp3_playlist(file_path):
    
    open_file = open(file_path, "r")
    file_content  = open_file.read()
    all_list = file_content.split(";")
    open_file.close()
    
    
    time_list = all_list[2::3].copy()
    sorted_times = sort_times(time_list) 
    offset = 2
    index = all_list.index(sorted_times[-1]) - offset
    longest_song = all_list[index]
    
    total_songs  = len(time_list)

    list_name = all_list[1::3].copy()
    
    top_band = find_name(list_name)
    longest_song = longest_song.strip()
    top_band = top_band.strip()
    anser = (longest_song ,total_songs, top_band)        
    return anser 
    
    
def add_text(file_path, new_song):
    open_file = open(file_path, "r")
    file_content  = open_file.read()
    all_list = file_content.split(";")
    open_file.close()
    while len(all_list) < 6:
        all_list.append(["\n"])
    
    all_list[6] = new_song
    return all_list
    
    #new_text = add_text(file_path, new_song)
    
def my_mp4_playlist(file_path, new_song):
    
    open_file = open(file_path, "r+")
    file_content  = open_file.read()
    all_list = file_content.split(";")

    while len(all_list) < 3:
        all_list.append("")
    
    all_list.insert(6, new_song)
    #all_list[2] = new_song
    all_text = ";".join(all_list)
    
    open_file.seek(0)
    open_file.write(all_text)
    open_file.seek(0)
    
    print(f"file: {open_file.read()}")
    open_file.close()
   

my_mp4_playlist(r"C:\work\python\files\songs.txt","Me: Why chat, when you can use an owl?" )

'''

def who_is_missing(file_name):
    #file_name.seek(0)
    file_string = open(file_name, "r")
    con = file_string.read()
    file_string.close()
    number = con.split(",")
    number = [int(num) for num in number]
    print(f"namber:{number}")
    number.sort()
    print(f"namber:{number}")
    
    
    size = number[0] + len(number)    
    i = 1
    w = 0
    while i < size:    
        print(f"namber:{number}, i: {i}, number[{w}]:{number[w]}")    
        if i != number[w]:
            print(f"ni: {i} != number[{w}]:{number[w]}")
            new_file = open(r"C:\work\python\files\found.txt", "w")
            new_file.write(str(i))
            print(f"i: {i}")    
            return i
        i+=1
        w+=1
        



print(who_is_missing(r"C:\work\python\files\findMe.txt"))



"""Finds a missing number in a sequence of numbers (un-sorted), read from a given file. Writes the missing number to a new file.
:param: file_name: path of the file contains th numbers
:type: string
:return: n: the missing number
:rtype: int
"""
def who_is_missing(file_name):
    fid = open(file_name, "r")
    line = fid.read()
    n_list = [int(n) for n in line.split(',')]
    fid.close()
    for n in range(1, len(n_list) + 2):
        if n not in n_list:
            fout = open("found.txt", "w")
            fout.write(str(n))
            return n

def copy_file_content(source, destination):
    copy = open(source, "r+")
    paste = open(destination, "+w")
    data = copy.read()
    paste.write(data)
    paste.seek(0)  # Move the file pointer to the beginning of the file
    print(paste.read())
    copy.close()
    paste.close()
    
copy = r"C:\work\python\files\file1.txt"
paste = r"C:\work\python\files\file2.txt"

copy_file_content(copy, paste)



rawData = "# sdf sdf %% df"

rawData = rawData.replace("\n", "")
sorted_data = sorted(set(rawData.split(" ")),key = ascii)

print(sorted_data)
    


path_input = input(r"enter a file path:")
task_input = input("Enter a task:")


if task_input == "sort":
    with open(path_input,'r') as file:
        rawData = file.read()
        rawData = rawData.replace("\n", "")
        sorted_data = sorted(set(rawData.split(" ")),key = ascii)

    print(sorted_data)
     

if task_input == "rev":
    with open(path_input,'r') as file:
        rawData = file.read()
        lines = rawData.split("\n")
        reversed_lines = [line[::-1] for line in lines]
        rev_data = "\n".join(reversed_lines)         
    print(rev_data)

if task_input == "last":
    number = int(input("Enter a number:"))
    with open(path_input,'r') as file:
        rawData = file.read()
        last_data = (rawData.split("\n"))
    print(last_data[-number:])


def are_files_equal(file1, file2):
    """
    Compares two files.

    :param file1: Path of the first file.
    :param file2: Path of the second file.
    :return: True if the files are equal, False otherwise.
    """
    content1 = open(file1, "r").read()
    content2 = open(file2, "r").read()

    return content1 == content2

    
file1 = r"C:\work\python\files\file1.txt"
file2 = r"C:\work\python\files\file2.txt"


are_files_equal(file1, file2)

def are_files_equal(file1, file2):
	with open(file1,'r') as input_file1, \
	     open(file2,'r') as input_file2:
			rawData1=input_file1.read()
			rawData2=input_file2.read()
			if (rawData1==rawData2):
				return True
			else:
				return False

#8

def combine_duplicate(list_tuple):
    list_copy = list_tuple.copy() 
    print(f"list_copy: {list_copy}")
    tmp = []
    
    for t in list_tuple: 

        
        i = 0
        
        new_list = []
        print(f"____t: {t} _____in_____new_list: {new_list}_____\n")  
        if t[-1] not in new_list and list_copy != []:
            print(f"_______start_____t: {t} _____in_____list_tuple: {list_tuple}_____\n")  
            
            new_list.append(list_copy[0])
            list_copy.remove(list_copy[0]) 
            size = len(list_copy) 
            
            while list_copy != []:
            
                print(f"____start________i:{i} ________in___size:{size}_____")  

                if list_copy[0][-1] == new_list[0][-1]:
                    print(f"in if: list_copy[0][-1]: {list_copy[0][-1]}, new_list[{i}][-1]: {new_list[i][-1]}")
                
                    new_list[0] = new_list[0][:-1] + list_copy[0]
                    print(f"list_copy: {list_copy} , new_list[{0}] = {new_list[0]}")
                list_copy.remove(list_copy[0])
                
                size = len(list_copy)
                 
                print(f"i:{i},size:{size} (len(list_copy))")
                print(f"____end________i:{i}__in__ size:{size}_____\n")    
                i +=1
            
            tmp.append(new_list[0])
            tmp.append(t)
            print(f"t: {t}, new_list: {new_list} list_copy: {list_copy}")             
                
            print(f"_______end_____t: {t}___in_____list_tuple: {list_tuple}_____\n")  
           
    
    print(f"______end______tmp__ {tmp}_____")  
    return tmp  
               
            
#8

my_dict = {'I': 3, 'love': 3, 'self.py!': 2}

list_tuple = [('I', 3), ('love',3), ('self.py!', 2)]

           
            
            
            


def combine_duplicate(list_tuple):
    new_list = []
    list_copy = list_tuple.copy()
    
    for t in range(len(list_tuple)):        
        for i in range(len(new_list)):

            if list_tuple[t][-1] == new_list[i][-1]:
                new_list.append(new_list[:-1] + list_tuple[t])
            else:
                new_list.append(list_tuple[t])
            list_copy.remove(list_tuple[t])
            
            




def combine_duplicate(list_tuple):
    tmp = -1
    new_list = []
    for t in list_tuple:
        for i in range(len(new_list)):
            
            if t[-1] == new_list[i][-1]:
                tmp = new_list[i][:-1] + t
            else:
                tmp = None
        if tmp is not None:
            new_list.append(tmp)
            
    return new_list

   
def combine_tuples(tuples: list[tuple]) -> list[tuple]:
   [sum([t1[:-1] for t1 in tuples if t1[-1] == key]) for key in set([t[-1] for t in tuples])]



def inverse_dict(my_dict):
    list_tuple = list()
    for i in my_dict.items():
        list_tuple.append(i)
    print(i)
    return list_tuple
list_tuple = inverse_dict(my_dict)


def combine_duplicate(list_tuple):
    merged_list = list_tuple.copy()
   
    if merged_list[0][1] == merged_list[1][1]:
        tump = (merged_list[0][0], merged_list[1][0], merged_list[0][1])
        merged_list.remove(merged_list[1])
        merged_list[0] = tump

    return merged_list
    
merged_list = combine_duplicate(list_tuple)



def tuple_list_to_dict(merged_list):
    dic_revers = {}
    for i in merged_list:
        dic_revers[i[-1]] = i[0:-1]
    return dic_revers

dic_revers = tuple_list_to_dict(merged_list)



def main():
    """
    The main functions
    """ 
    my_dict = {'I': 3, 'love': 3, 'self.py!': 2}

    list_tuple = inverse_dict(my_dict)

    merged_list = combine_duplicate(list_tuple)

    dic_revers = tuple_list_to_dict(merged_list)
    print(f"dic_revers{}",dic_revers)
    
    
if __name__ == "__main__":
    main()



def inverse_dict(my_dict):
    dic_temp = {}
    
    for value in my_dict.values():
        for key in my_dict.keys():
            if value not in dic_temp:
                dic_temp[value] = key
            else:
                dic_temp[value] = my_dict[key]
         
            print(value, dic_temp[value] , key)   
            if key == dic_temp[value]:
                dic_temp[value]= key

    return dic_temp

def inverse_dict(my_dict):
    list_tuple = []
    for item in my_dict.items():
        if item[1] in [x[1] for x in my_dict.items() if x != item]:
            new_item = ([x[0] for x in my_dict.items() if x[1] == item[1]][0], item[0] ,item[1])
            list_tuple.append(new_item)
        else:
            list_tuple.append(item)

    list_tuple = [item for item in list_tuple if item[1] != item[0]]
   
    dic_temp = {} 
    for t in list_tuple:
        dic_temp[list_tuple[:-1]] = [list_tuple[-1]]
        

    return dic_temp
    
inverse_dict({'I': 3, 'love': 1, 'self.py!': 2})
inverse_dict({'I': 3, 'love': 3, 'self.py!': 2})



    
-------------------












________----------

def sort_anagrams(list_of_strings):   
    cop = list_of_strings.copy()
    res = []
    for l in list_of_strings:
        seved_elemets = []
        for element in cop: 
            if sorted(l) == sorted(element):
                seved_elemets.append(element)
                
        for l in seved_elemets:
            cop.remove(l)  
        
        if seved_elemets: 
            res.append(seved_elemets)   

    return res

def count_chars(my_str): 
   """Counts the occurrences of each character in a string, ignoring spaces.
    :param my_str: The input list of characters.
    :type my_str: list
    :return: A dictionary where each key-value pair represents a character and its frequency in the list.
             The format of each pair is [char, freq].
    :rtype: dict
    """
   return {char: my_str.count(char) for char in my_str.replace(" ","")}


def dipnum():

dic_nari = {'first_name': 'Mariah', 'last_name':'Carey', 'birth_date':'27.03.1970', 'hobbies':['Sing', 'Compose', 'Act']}
num = int(input("number 1-7"))

if num == 1:
    print(dic_nari['last_name'])
if num == 2:    
    print(dic_nari['birth_date'])     
if num == 3:
    print(len(dic_nari['hobbies']))
if num == 4:
    temp_list = dic_nari['hobbies']
    print(temp_list[-1])
if num == 5:
    temp_list = dic_nari['hobbies'] + ['Cooking']
    dic_nari['hobbies'] = temp_list
    print(dic_nari['hobbies'])
if num == 6: 
    dic_nari['birth_date'] = (27, 3, 1970)
    print(dic_nari['birth_date'])
if num == 7:
    dic_nari['age'] = 52
    print(dic_nari['age'])
        




    if num == 5:    
        print("list_of_strings: ",list_of_strings, "\n new_list", new_list)

def mult_tuple(tuple1, tuple2):
    ""
    Create tuples with all possible combinations of elements from tuple1 and tuple2.

    :param tuple1: The first tuple.
    :type tuple1: tuple
    :param tuple2: The second tuple.
    :type tuple2: tuple
    :return: A tuple of tuples representing all possible combinations.
    :rtype: tuple
    """
    new_tap = ()
    
    for t1 in tuple1:
        for t2 in tuple2:
            if t1 == t2:
                new_tap += ((t1 , t2),)
            else:
                new_tap += ((t1 , t2),)
                new_tap += ((t2 , t1),)          
    return new_tap

def mult_tuple(tuple1, tuple2):
    """Builds all possible couples of the given 2 tuples
    :params: tuple1, tuple2: input touples
    :return: tuple contains all the couples. Order not mandatory
    :rtype: tuple
    """
    calc = tuple([(t1, t2) for t1 in tuple1 for t2 in tuple2])
    return calc + tuple([p[::-1] for p in calc])
def sort_prices(list_of_tuples):
    """Sorts items according to their price, from higher to lower.
    :param: list_of_tuples: the input list, each tuple contains an item and its
    price
    :param: list of tuples. price is double
    :return: sorted list
    :rtype: list of tuples.
    """
    return sorted(list_of_tuples, key = lambda x: x[1], reverse = True) 

data = ("self", "py", 1.543)
format_string = "Hello %s.%s learner, you have only %.1f units left before you master the course!"

print(format_string % data)


def mult_tuple(tuple1, tuple2):
    return (t in tuple1 ,)

first_tuple = (1, 2)
second_tuple = (4, 5)

print(mult_tuple(first_tuple, second_tuple))
def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key = lambda x: x[1] , reverse=True)


def sort_prices(list_of_tuples):
    """Sorts items according to their price, from higher to lower.
    :param: list_of_tuples: the input list, each tuple contains an item and its
    price
    :param: list of tuples. price is double
    :return: sorted list
    :rtype: list of tuples.
    """

    list_of_tuples.sort(key=lambda x: x[1])
    list_of_tuples.reverse()
    return list_of_tuples


data = ("self", "py", 1.543)
format_string ='{} {}.{} {}, {} {:.1f} {}'.format("Hello", data[0], data[1],"learner" , "you have only", data[2], "units left before you master the course!")

print(format_string)





def arrow(my_char, max_length):
    """
    Prints an arrow pattern using a specified character.

    :param my_char: The character to be used in the arrow pattern.
    :type my_char: str
    :param max_length: The maximum length of the arrow pattern.
    :type max_length: int
    """
    tmp_char = ""
    
    for i in range(1, max_length):
        tmp_char += my_char*i + '\n'
        
     
    for i in range(max_length, 0, -1):
        tmp_char += my_char*i + '\n'
    
    return tmp_char[:-1]    
        
    

def main():
    """
    The main function that executes the program.
    """ 
    
    print(arrow('D',1))
    print(arrow('*',5))	
    
    
if __name__ == "__main__":
    main()

def process_options(products_list):
    """
    This function processes the user's input options.
    :param products_list: The list of products.
    :type products_list: list
    """
    digit = 1
    while (digit != 9):
        digit = take_digit()
        
        if digit == 1:
            print(products_list)
            
        elif digit == 2:
            print(len(products_list))
            
        elif digit == 3:     
            print(bool(element_in_list(products_list)))
            
        elif digit == 4:
            print(element_in_list(products_list))
                
        elif digit == 5:
            product = str(input("Please enter a product name"))
            if product in products_list:
                products_list.remove(product)
          
        elif digit == 6:
            product = str(input("Enter a product you want to append to the list."))
            products_list.append(product)
            
        elif digit == 7:
            for product in products_list:
                if len(product) < 3 or not product.isalpha():
                    print(product)     
                    
        elif digit == 8:
            for product in products_list:
                while products_list.count(product) > 1:
                    products_list.remove(product)            

def element_in_list(products_list):
    product = str(input("Please enter a product name"))
    return products_list.count(product)
        

def take_digit():
    """
    This function takes user input for a digit between 1 and 9.
    :return: The chosen digit.
    :rtype: int
    """
    digit = int(input("Enter a digit between 1 and 9:"))
    return digit

def main():
    """
    The main function that executes the program.
    """ 
    products = str(input("Insert a list of products."))
    products_list = products.split(",")
    process_options(products_list)
    print("Good By")
    
    
if __name__ == "__main__":
    main()

def sequence_del(my_str):
    """Deletes all letter duplicates in the input string.
    :param my_str: input string
    :type my_str: string.
    :return: the input string, without duplicates (one letter out of each sequence)
    :rtype: string.
	"""
    if len(my_str) > 0:
        result = my_str[0]
        for char in my_str[1:]:
            if char != result[-1]:
                result = result + char
        return result
    return my_str


def sequence_del(my_str):
    """The function that removes duplicate characters.
    :param my_str: The received string.  
    :type my_str: String     
    :return: Returns a string with one occurrence of each character.
    :rtype: String
    """
    new_list = []

    for n in my_str:
        if n not in new_list: 
            new_list.append(n) 
    new_str = ''.join(new_list)
    return new_str   
      

def main():
    # Call the function sequence_del
    my_str = sequence_del("ppyyyyythhhhhooonnnnn")
    print(my_str)
    
    
if __name__ == "__main__":
    main()

def seven_boom(end_number):
    """""" The function that simulates the game "Seven Boom". 
    :param end_number: An integer number.  
    :type end_number: int     
    :return: a list within the range of numbers from 0 to end_number, inclusive, where each number that satisfies certain conditions is replaced with the string "BOOM".
    :rtype: list
    """
    #new_list = range(end_number)
    new_list = [None]*(end_number+1)
    for n in range(end_number+1):
        if ((n%7) == 0) or '7' in str(n):
            new_list[n] = "BOOM"
        else:
            new_list[n] = (n)        
    return new_list    
       
def main():
    # Call the function numbers_letters_count
    list_n = seven_boom(17)
    print(list_n)
    
    
if __name__ == "__main__":
    main()

        
def numbers_letters_count(my_str):
    """ The function receives a string 
    and returns a list with two elements: the number of digits and the number of letters in the string (including non-alphanumeric characters).
    :param my_list: A string on which tests are performed. 
    :type my_list: string     
    :return: a list with two elements: the number of digits and the number of letters in the string (including non-alphanumeric characters).
    :rtype: a list of two int.
    """
    list_count = [0, 0]
    for char in my_str:
        if char.isnumeric():
            list_count[0] += 1
        else:
           list_count[1] += 1
    return list_count   
       
def main():
    # Call the function numbers_letters_count
    print(numbers_letters_count("Python 3.6.3"))

if __name__ == "__main__":
    main()

def is_greater(my_list, n):
    """ 
    :param my_list: list of number
    :param n: The number to which "my_list" numbers are compared.
    :type my_list: a list of numbers     
    :type n: float
    :return: A new list with all the elements greater than the number n..
    :rtype: list
    """
    new_list = []
    for element in my_list:
        if n < element:
            new_list.append(element)
    return new_list

def main():
    # Call the function is_greater
    result = is_greater([1, 30, 25, 60, 27, 28], 28)
    print(result)

if __name__ == "__main__":
    main()




def squared_numbers(start, stop):
    """ Returns a list of squares of numbers between start and stop(inclusive).
    :param start:The starting number.
    :param start:The ending number.
    :type start: int    
    :type stop: int    
    :return:  A list of squared numbers.
    :rtype: list
    """
    rlist = []
    while start <= stop:
        rlist.append(start**2)
        start += 1  
    return rlist
    
    
    
print(squared_numbers(-3, 3))
def longest(my_list):
    """The function takes a list of strings and returns the longest string.
    :param my_list:list of strings
    :type list1: list
    :return: the longest string.
    :rtype: string
    """
    longest_string = sorted(my_list, key = len)
    return longest_string[-1]

def main():
    # Call the function longest
    list1 = ["111", "234", "2000", "goru", "birthday", "09"]
    print(longest(list1))

if __name__ == "__main__":
    main()





def are_lists_equal(list1, list2):
    """The function compares two lists of numbers(int and float only)and returns True or false
    :param list1:list of mumber(int and float only)
    :param list2: list of mumber(int and float only)
    :type list1: list
    :type list2: list
    :return: True if they are identical (even if in a different order), 
    otherwise it returns False.
    :rtype: bool
    """
    if len(list1) == len(list2):
        list1.sort()
        list2.sort()
        print(list1 , list2)
        return list1 == list2
    return False
    
    
def main():
    # Call the function are_lists_equal
    list1 = [0.6, 1, 2, 3]
    list2 = [3, 2, 0.6, 1]
    print(are_lists_equal(list1, list2))

if __name__ == "__main__":
    main()

    
def extend_list_x(list_x, list_y):
    """The function appends `list_y` to the beginning of `list_x` 
    and returns the modified `list_x`.
    :param list_y: A string that is contained within another string.
    :param list_x:A string that contains the second string. 
    :type list_x: list
    :type list_y: list
    :return: expands list_x by adding list_y at the beginning, 
    and returns list_x
    :rtype: list
        """
    list_x[:0] = list_y
    return list_x


def main():
    # Call the function extend_list_x
    x = [4, 5, 6]
    y = [1, 2, 3]
    print(extend_list_x(x,y))

if __name__ == "__main__":
    main()





def format_list(my_list):
    ''''''The function takes a list of even-length strings. 
    It returns a string that includes the elements of the list at even positions,
    separated by commas and spaces, 
    and also the last element preceded by the word "and".
    :param my_list: List of even-length strings
    :type my_list: list
    :return:A string containing the elements of the list at even positions, separated by commas and spaces, and additionally the last element preceded by the word "and".
    :rtype: string
    
    
    return ", ".join(my_list[::2] + ["and " + my_list[-1]]) 
    

def main():
    # Call the function format_list
    my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]    
    print(format_list(my_list))

if __name__ == "__main__":
    main()
    
    


def shift_left(my_list):
   ''' '''The function takes a list of length 3 and returns a new list shifted one step to the left.
    :param my_list: list of length 3
    :type my_list: list
    :return:a new list shifted one step to the left.
    :rtype: list
 '''   '''
    return [my_list[1],my_list[2] ,my_list[0]] 
    
    
def main():
    # Call the function shift_left
    print(shift_left([0, 1, 2]))

if __name__ == "__main__":
    main()


def func(num1, num2):
    """Equal a nambers 
    : param nam1: number 1 for the equal
    : param num2: number 2 for the equal
    : type num1: int
    : type num2: int
    : return: The result of boolean if the numbers is equal
    : rtype: bool  
    """
    return num1 == num2


def main():
    # Call the function func
    print(func(1,2))

if __name__ == "__main__":
    main()


def chocolate_maker(small, big, x):
    return x <= big*5 + small

print(chocolate_maker(3, 1, 8),
chocolate_maker(3, 1, 9),
chocolate_maker(3, 2, 10))

def filter_teens(a=13, b=13, c=13):
    age1 = fix_age(a)
    age2 = fix_age(b)
    age3 = fix_age(c)
    return age1 + age2 + age3


def fix_age(age):
    if age >= 13 and age <= 19 and age != 15 and age != 16:
        return 0
    return age

    
print(
filter_teens(),
filter_teens(1, 2, 3),
filter_teens(2, 13, 1),
filter_teens(2, 1, 15))


def distance(num1, num2, num3):  
    return((abs(num1 - num2) == 1 or abs(num1 - num3) == 1)
    and ((2 <= abs(num1 - num2) and 2 <= abs(num3 - num2))
    or (2 <= abs(num2 - num3) and 2 <= abs(num1 - num3))))


 
print(distance(0,2,1))



        abs(num2 + 2) >= abs(num1 and num3)) or (abs(num1 + 2) >= (abs(num2) and abs(num3))) or (abs(num3 + 2) >= (abs(num1) and abs(num2)))):
               (2 >= abs(num1 - num2))and  or (abs(num1 - num3)) == 1)):
    print(abs(num1 - num2), abs(num1 - num3))
    print("((abs(num1 - num2) or abs(num1 - num3)) == 1)" , ((abs(num1 - num2) or abs(num1 - num3)) == 1))
    print("num1 + 2 >= (num2 and num3))", num1 + 2 >= (num2 and num3))
0 1 10
11 1 10
0 5 -5
0 -1 1
0 2 1
    if ((abs(num1 - num2) or abs(num2 - num1)) == 1 ) and ((abs(num1 - num2) or abs(num2 - num1)) >= abs(num3 + 2)):
        return True
    elif((abs(num1 - num3) or abs(num3 - num1)) == 1 ) and ((abs(num1 - num3) or abs(num3 - num1)) >= abs(num2 + 2)):
        return True
    num1 = abs(num1)
    num2 = abs(num2)
    num3 = abs(num3)
    if (num1 + 1 == num2):
        return ((num1 + 2 and num2 + 2) or  <= num3)
    elif (num1 + 1 == num3):
        return ((num1 + 2 and num3 + 2) <= num2)
print(distance(4, 5, 3))

def last_early(my_str):
    my_str = my_str.lower()
    sefix_my_str = my_str[-1]
    prefix_my_str = my_str[:-1]
    return(prefix_my_str.rfind(sefix_my_str)!= -1)
    
last_early("happy birthday")   
 
import calendar
date_format = input('Enter a date: ')

day = int(date_format[:2])
month = int(date_format[3:5])
year = int(date_format[6:])

number_day = calendar.weekday(year, month, day)
print(calendar.day_name[number_day])

x = "fsdf"
if(len(X) > 1 and x.isalpha()):
    print('E3')
elif (len(X) > 1):
    print('E1')
elif(x.isalpha()):
    print('E2')




F_or_C = input('Insert the temperature you would like to convert: ').lower()

print(F_or_C)
bool_tmp = F_or_C.endswith('f')
print(bool_tmp)

if bool_tmp:  
    print(((5 * float(F_or_C[:-1])) - 160) / 9 , 'C')
else:
    print(((9 * float(F_or_C[:-1])) + (32 * 5)) / 5 , 'F')





is_polindrom = input('Enter a word: ')

is_polindrom = is_polindrom.replace(' ', '').lower()
print(is_polindrom)
if is_polindrom[::1] == is_polindrom[::-1]:
    print('OK')
else:
    print('NOT')
        



str_swith = input('Please enter a string: ')
size_str = len(str_swith)
prefix_str = str_swith[:int((size_str)/2)]
size_prefix = len(prefix_str)
sefix_str = str_swith[size_prefix:]
print(prefix_str.lower() + sefix_str.upper())


str_swith_e = input('Please enter a string: ')
temp = str_swith_e[0]
str_place_1 = str_swith_e[1:]
print(temp + str_place_1.replace(temp, 'e'))



encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
print(encrypted_message[-1:0:-2])
encrypted_message[-1::-2]

'''