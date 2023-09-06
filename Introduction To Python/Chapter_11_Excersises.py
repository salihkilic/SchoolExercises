# Things to do, chapter 11
# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch11.html#idm45794991636984

from CustomImports import zoo
from CustomImports import zoo as menagerie
from CustomImports.zoo import hours
from CustomImports.zoo import hours as info

from collections import OrderedDict, defaultdict

# 11.1 Create a file called zoo.py. In it, define a function called hours() that prints the string 'Open 9-5 daily'.
# Then, use the interactive interpreter to import the zoo module and call its hours() function.
print("\n------ 11.1 ------")
# Please note the first import statement at the top of this file. The zoo function is in a file in a folder called
# "CustomImports", the exercise wants us to create it there and call it here.
zoo.hours()


# 11.2 In the interactive interpreter, import the zoo module as menagerie and call its hours() function.
print("\n------ 11.2 ------")
# Please note the second import statement at the top of this file
menagerie.hours()


# 11.3 Staying in the interpreter, import the hours() function from zoo directly and call it.
print("\n------ 11.3 ------")
# Please note the third import statement at the top of this file
hours()


# 11.4 Import the hours() function as info and call it.
print("\n------ 11.4 ------")
# Please note the fourth import statement at the top of this file
info()


# 11.5 Make a dictionary called plain with the key-value pairs 'a': 1, 'b': 2, and 'c': 3, and then print it.
print("\n------ 11.5 ------")

plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)


# 11.6 Make an OrderedDict called fancy from the same pairs listed in the previous question and print it. Did it
# print in the same order as plain?
print("\n------ 11.6 ------")

fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(f"Normal Dict: {plain}")
print(f"Ordered Dict: {fancy}")
print("Info: Starting with Python 3.7, dicts are ordered by default. There will be no difference between these two by "
      "default")


# 11.7 Make a defaultdict called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and
# append the value 'something for a' to it in one assignment. Print dict_of_lists['a'].
print("\n------ 11.7 ------")
dict_of_lists = defaultdict(list)
dict_of_lists["a"].append("something for a")
print(dict_of_lists)
print(dict_of_lists["a"])
