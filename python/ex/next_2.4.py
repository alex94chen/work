class BigThing ():

    def __init__(self, x = 0):
        self._x = x

    def size(self):
        if isinstance(self._x, int):
            return self._x
        else:
            return len(self._x) 
        
class BigCat(BigThing ):
    def __init__(self, x=0, weight = 0):
        super().__init__(x)
        self._weight = weight

    def size(self):
        super().size()
        if self._weight > 20:
            return "Very Fat"
        elif self._weight > 15:
            return "Fat"
        else:
            return "OK"
        

def main():
    cutie = BigCat("mitzy", 22)
    print(cutie.size())

if __name__ == "__main__":
    main()