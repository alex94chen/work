class Animal():
    """
    A base class representing an animal.

    Attributes:
        zoo_name (str): A class attribute holding the name of the zoo.
        _name (str): The name of the animal.
        _hunger (int): The hunger level of the animal.
    """
     
    zoo_name = "Hayaton"

    def __init__(self, name, hunger =0):
        """
        Initializes an Animal object.

        Args:
            name (str): The name of the animal.
            hunger (int, optional): The initial hunger level. Defaults to 0.
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """
        Returns the name of the animal.

        Returns:
            str: The name of the animal.
        """
        return self._name
    
    def is_hungry(self):
        """
        Checks if the animal is hungry.

        Returns:
            bool: True if the animal is hungry, False otherwise.
        """
        return self._hunger > 0

    def food(self):
        """
        Decreases the animal's hunger level by 1.
        """
        self._hunger = self._hunger - 1

    def talk(self):
        """
        Makes the animal perform a vocalization.
        (To be overridden by subclasses)
        """
        pass



    def special_method(self):
        """
        Performs a special action specific to the animal.
        (To be overridden by subclasses)
        """
        pass	



class Dog(Animal):
    """
    A class representing a dog, inheriting from Animal.
    """
    
    def __init__(self, name, hunger=0):
        """
        Initializes a Dog object.

        Args:
            name (str): The name of the dog.
            hunger (int, optional): The initial hunger level. Defaults to 0.
        """
        super().__init__(name, hunger)

    def tolk(self):
        """
        Makes the dog bark.
        """
        print("woof woof")

    def fetch_stick(self):
        """
        Makes the dog fetch a stick.
        """
        print("There you go, sir!")   
        
    def special_method(self):
        """
        Makes the dog perform a special action: fetch a stick.
        """
        self.fetch_stick()	 


class Cat(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def tolk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")
    
    def special_method(self):
        self.chase_laser()	

class Skunk(Animal):
    def __init__(self, name, hunger=0, stink_count = 6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def tolk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")
    
    def special_method(self):
        self.stink()

class Unicorn(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def tolk(self):
        print("Good day, darling")
    
    def sing(self):
        print("I'm not your toy...")

    def special_method(self):
        self.sing()

class Dragon(Animal):
    def __init__(self, name, hunger=0, color = "Green"):
        super().__init__(name, hunger)
        self._color = color

    def tolk(self):
        print("Raaaawr")  

    def breath_fire(self):
        print("$@#$#@$")

    def special_method(self):
        self.breath_fire()

def main():
    """
    The main function that simulates the zoo.
    """
    zoo_lst = [Dog("Brownie", 10),Cat("Zelda", 3),Skunk("Stinky"), Unicorn("Keith", 7),Dragon("Lizzy", 1450)]
    zoo_lst.append(Dog("Doggo", 80))
    zoo_lst.append(Cat("Kitty", 80)) 
    zoo_lst.append(Skunk("Stinky Jr.", 80))
    zoo_lst.append(Unicorn("Clair", 80))
    zoo_lst.append(Dragon("McFly", 80))

    for animal in zoo_lst:
        print(f"{type(animal).__name__} {animal.get_name()}")

        while animal.is_hungry():
            animal.food()
        animal.tolk()
        animal.special_method() 
    print(Animal.zoo_name)


if __name__ == "__main__":
    main()


