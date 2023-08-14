#3.1

def error_StopIteration(y = [1,2]):
    x = iter(y)
    
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())


def error_ZeroDivisionError():
    return 5/0

def error_AssertionError():
    assert 1 == 0

def error_ImportError():
     import non_existent_module 

def error_KeyError():
    dic1 = {1:7 , 3: 6}
    return dic1[2]

def error_SyntaxError(): 
    a = (7 +)


    

def error_IndentationError():
   return 3

def error_TypeError():
    return 3 + 'd'

def main():


    error_StopIteration()
    error_ZeroDivisionError()
    error_AssertionError()
    error_ImportError()
    error_KeyError()
    # error_SyntaxError()
    error_IndentationError()
    error_TypeError()
  


if __name__ == "__main__":
    main()

