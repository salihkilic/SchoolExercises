# Things to do, chapter 10
# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch10.html#idm45794994281816

# 10.1 Make a class called Thing with no contents and print it. Then, create an object called example from this class
# and also print it. Are the printed values the same or different?
print("\n------ 10.1 ------")


class Thing:
    pass


# Print the class itself
print(Thing)

# Create an instance/Object of the class and print it
thing_instance = Thing()
print(thing_instance)

# Are they the same?
print(f"Are they the same: {Thing == thing_instance}")

# 10.2 Make a new class called Thing2 and assign the value 'abc' to a class attribute called letters. Print letters.
print("\n------ 10.2 ------")


class Thing2:
    letters = "abc"


print(Thing2.letters)

# 10.3 Make yet another class called, of course, Thing3. This time, assign the value 'xyz' to an instance (object)
# attribute called letters. Print letters. Do you need to make an object from the class to do this?
print("\n------ 10.3 ------")


class Thing3:
    def __init__(self):
        self.letters = "xyz"


# This will not work, but we're showing why
try:
    print(Thing3.letters)
except AttributeError as e:
    print(e)

# This will work, because we need to create an instance to access its variable
thing3_instance = Thing3()
print(thing3_instance.letters)

# 10.4 Make a class called Element, with instance attributes name, symbol, and number. Create an object of this class
# with the values 'Hydrogen', 'H', and 1.
print("\n------ 10.4 ------")


class Element:
    # If you are confused about the :str and :int used here, look up type-hints for python.
    def __init__(self, name: str, symbol: str, number: int):
        self.name = name
        self.symbol = symbol
        self.number = number


hydrogen = Element("Hydrogen", "H", 1)
print(f"Name: {hydrogen.name}\n"
      f"Symbol: {hydrogen.symbol}\n"
      f"Number: {hydrogen.number}")

# 10.5 Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1. Then,
# create an object called hydrogen from class Element using this dictionary.
print("\n------ 10.5 ------")

hydrogen_dict = {"name": "Hydrogen",
                 "symbol": "H",
                 "number": 1}

hydrogen = Element(hydrogen_dict["name"], hydrogen_dict["symbol"], hydrogen_dict["number"])
print(f"We created a Hydrogen element from this dict: {hydrogen_dict} \n")

# To check if it worked:
print(f"Name: {hydrogen.name}\n"
      f"Symbol: {hydrogen.symbol}\n"
      f"Number: {hydrogen.number}")

# 10.6 For the Element class, define a method called dump() that prints the values of the object’s attributes (name,
# symbol, and number). Create the hydrogen object from this new definition and use dump() to print its attributes.
print("\n------ 10.6 ------")


class Element:
    def __init__(self, name: str, symbol: str, number: int):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(f"Element dump: {self.name}, {self.symbol}, {self.number}")


upgraded_element = Element("Hydrogen", "H", 1)
upgraded_element.dump()

# 10.7 Call print(hydrogen). In the definition of Element, change the name of the method dump to __str__,
# create a new hydrogen object, and call print(hydrogen) again.
print("\n------ 10.7 ------")


class Element:
    def __init__(self, name: str, symbol: str, number: int):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f"This element is {self.name}, its symbol is {self.symbol} and it's periodic number is {self.number}"


string_instance = Element("Hydrogen", "H", 1)
print(string_instance)

# 10.8 Modify Element to make the attributes name, symbol, and number private. Define a getter property for each to
# return its value.
print("\n------ 10.8 ------")


class Element:
    def __init__(self, name: str, symbol: str, number: int):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    # -------- NAME getter/setter
    @property
    def name(self):
        print(f"Retrieved name: {self.__name}")
        return self.__name

    @name.setter
    def name(self, name):
        print(f"Set name: {self.__name} to {name}")
        self.__name = name

    # -------- SYMBOL getter/setter
    @property
    def symbol(self):
        print(f"Retrieved symbol: {self.__symbol}")
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol):
        print(f"Set symbol: {self.__symbol} to {symbol}")
        self.__symbol = symbol

    # -------- NUMBER getter/setter
    @property
    def number(self):
        print(f"Retrieved number: {self.__number}")
        return self.__number

    @number.setter
    def number(self, number):
        print(f"Set number: {self.__number} to {number}")
        self.__number = number


# Let's create the object to prove that we did these things right
get_set_element = Element("Hydrogen", "H", 1)

# Test Name
test = get_set_element.name
get_set_element.name = "Carbon"
print("--")

# Test Symbol
test = get_set_element.symbol
get_set_element.symbol = "C"
print("--")

# Test Number
test = get_set_element.number
get_set_element.number = "6"

# 10.9 Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). This should
# return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe). Create one object from each and print what
# it eats.
print("\n------ 10.9 ------")


class Bear:
    def eats(self):
        return "berries"


class Rabbit:
    def eats(self):
        return "clover"


class Octothorpe:
    def eats(self):
        return "campers"


# Create the instances and print what the eats() function returns
bear_instance = Bear()
print(bear_instance.eats())

rabbit_instance = Rabbit()
print(rabbit_instance.eats())

octothorpe_instance = Octothorpe()
print(octothorpe_instance.eats())

# 10.10 Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does(). This returns
# 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (SmartPhone). Then, define the class Robot that has one instance
# (object) of each of these. Define a does() method for the Robot that prints what its component objects do.
print("\n------ 10.10 ------")


class Laser:
    def does(self):
        return "Disintegrate!"


class Claw:
    def does(self):
        return "Crush!"


class SmartPhone:
    def does(self):
        return "Ring Ring!"


class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.phone = SmartPhone()

    def does(self):
        print(self.laser.does())
        print(self.claw.does())
        print(self.phone.does())


# Show off our fancy robot
bleep_bloop = Robot()
bleep_bloop.does()
