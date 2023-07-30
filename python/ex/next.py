


#1.3.1
def intersection(list_1, list_2):
    pass




#1.2.5

import functools
def function(num, item):
    return num + 1
    
    
password = input("Enter Your password (integers only): ")


lst = list(map(int, password))


magic = functools.reduce(function, lst)


result = (lambda x: x % 4 == 0)(magic)


if result:
    print("Correct password!")
else:
    print("Wrong password.")
    
    
    
    
    


#1.2.4
d = lambda x, y: y
print(d(1, 3))
print(d(5, 2))
#1.2.3

c = lambda x, y:x + y
print(c(1, 3))
print(c(2, 5))

#1.2.2

b = lambda x: x
print(b(1))
print(b(3))


#1.2.1 
a = lambda x: 1

print(a(3))
print(a("s"))
print(a(2))
print(type(a(3)))




#1.1.4
from functools import reduce

def sum_dig(x, y):
    return int(x) + int(y)
    
    
def sum_of_digits(number):
    return reduce(sum_dig, list(str(number)))

print(sum_of_digits(45))

def test_sum_of_digits():
    assert sum_of_digits(56) == 9
    assert sum_of_digits(10000004) == 5
    assert sum_of_digits(0) == 0

#1.1.3
#my
def four_dividers(number):
    return list(filter(div, range(number)))

def div(num):
    if num%4 == 0:
        return num


print(four_dividers(9))
print(four_dividers(3))

def test_four_dividers():
    assert four_dividers(56) == [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52]
    assert four_dividers(0) == []



#1.1.2
#my
def double_letter(my_str):
   return ''.join(list(map(f, my_str)))
   
def f(i):
    return(i + i)
    
print(double_letter("python"))
import pytest
def test_double_letter():
    assert double_letter("python") == 'ppyytthhoonn'
    assert double_letter("") == ''
    assert double_letter("we are the champions!") == 'wwee  aarree  tthhee  cchhaammppiioonnss!!'


# 1.0
#my
def combine_coins (coin, numbers):
    return ' '.join((coin + str(num)) for num in numbers)
    
print(combine_coins('$', range(5)))
    
def combine_coins(coin, numbers):
    output = ""
    for num in numbers:
        output += coin + str(num) + ', '
     # Ignore the last comma.
    return output[:-2]