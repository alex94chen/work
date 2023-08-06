class Dolfin:
    count_animals  = 0 

    def __init__(self, name = 'Octavio'):
        self._name = name
        self._age = 4
        Dolfin.count_animals += 1 


    def birthday(self):
        self._age += 1
    
    def get_age(self):
        return self.age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

def main():
    dolfin1 = Dolfin("Mami")
    dolfin2 = Dolfin()
    print(dolfin1.get_name(), dolfin2.get_name())
    dolfin2.set_name("Dolfi")
    print(dolfin1.get_name(), dolfin2.get_name())
    print(Dolfin.count_animals)

if __name__ == "__main__":
    main()
