from functools import reduce

def long_name(names_txt):
    """Find the longest name in the given text file."""
    return reduce(lambda x, y: x if len(x) > len(y) else y, open(names_txt, 'r').read().split())  

def total_name_length(names_txt):
    """Calculate the sum of the lengths of all names in the given text file."""
    return reduce(lambda x, y: x + y, [len(name) for name in open(names_txt, 'r').read().split()])   

def small_name(names_txt):
    """Find the shortest names in the given text file."""
    return "\n".join(filter(lambda name: len(name) == min(len(name) for name in [name.strip() for name in open(names_txt, 'r').read().split()]), [name.strip() for name in open(names_txt, 'r').read().split()]))

def write_name_lengths(names_txt):
    """Write the lengths of all non-empty names to a new text file."""
    with open(r"c:\work\python\ex\name_length.txt", 'w') as file:
        file.write("\n".join(str(length) for length in [len(name.strip()) for name in open(names_txt, 'r').read().split() if len(name.strip()) > 0]))

def find_names_by_length(names_txt):
    """Find all names in the given text file with a specific length."""
    num = int(input("Please enter a number: "))
    return "\n".join(filter(lambda name: num == len(name), [name.strip() for name in open(names_txt, 'r').read().split()]))

def main():
    names_txt = "names.txt"
    print("long_name:\n", long_name(names_txt))
    
    print("total_name_length:\n", total_name_length(names_txt))
    
    print("small_name:\n", small_name(names_txt))
    
    print("num_name:\n", find_names_by_length(names_txt))
    
    write_name_lengths(names_txt)

if __name__ == "__main__":
    main()
