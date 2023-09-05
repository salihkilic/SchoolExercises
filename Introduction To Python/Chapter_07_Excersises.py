# Things to do, chapter 7
from random import randint

# Use lists and tuples with numbers (Chapter 3) and strings (Chapter 5) to represent elements in the real world with
# great variety.

# 7.1 Create a list called years_list, starting with the year of your birth, and each year thereafter until the year
# of your fifth birthday. For example, if you were born in 1980, the list would be years_list = [1980, 1981, 1982,
# 1983, 1984, 1985]. If you’re less than five years old and reading this book, I don’t know what to tell you.
print("\n------ 7.1 ------")

# Let's pick a random year between 1970 an 2000
year_list = [randint(1970, 2000)]
for x in range(5):
    # This grabs the last element in the list, adds 1 to it and appends it to the list
    year_list.append(year_list[-1] + 1)

print(f"Starting year: {year_list[0]}")
print(year_list)


# 7.2 In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.
print("\n------ 7.2 ------")
print(f"We were three years old in {year_list[3]}")


# 7.3 In which year in years_list were you the oldest?
print("\n------ 7.3 ------")
print(f"We were the oldest in {year_list[-1]}")


# 7.4 Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
print("\n------ 7.4 ------")
things = ["mozzarella", "cinderella", "salmonella"]
print(things)


# 7.5 Capitalize the element in things that refers to a person and then print the list. Did it change the element in
# the list?
print("\n------ 7.5 ------")
print(f"Before: {things}")
things[1] = things[1].capitalize()
print(f"After: {things}")


# 7.6 Make the cheesy element of things all uppercase and then print the list.
print("\n------ 7.6 ------")
print(f"Before: {things}")
things[0] = things[0].swapcase()
print(f"After: {things}")


# 7.7 Delete the disease element from things, collect your Nobel Prize, and print the list.
print("\n------ 7.7 ------")
print(f"Before: {things}")
del things[2]
print("I would like to thank my mom and the scientific community for this achievement")
print(f"After winning nobel prize: {things}")


# 7.8 Create a list called surprise with the elements "Groucho", "Chico", and "Harpo".
print("\n------ 7.8 ------")
surprise = ["Groucho", "Chico", "Harpo"]


# 7.9 Lowercase the last element of the surprise list, reverse it, and then capitalize it.
print("\n------ 7.9 ------")
# This uses the power of chaining
surprise[-1] = surprise[-1].lower()[::-1].capitalize()
print("Chained:")
print(surprise)

# Above is the same as the following:
surprise = ["Groucho", "Chico", "Harpo"]
surprise[-1] = surprise[-1].lower()         # Lowercase it
surprise[-1] = surprise[-1][::-1]           # Reverse it
surprise[-1] = surprise[-1].capitalize()    # Capitalize it
print("Not chained")
print(surprise)


# 7.10 Use a list comprehension to make a list called even of the even numbers in range(10).
print("\n------ 7.10 ------")
# The modulo operator (%) is quite handy for cases like this
my_list = [x for x in range(10) if x % 2 == 0]
print(my_list)


# 7.11 Let’s create a jump rope rhyme maker. You’ll print a series of two-line rhymes. Start with this program fragment:

# For each tuple (first, second) in rhymes:
#
# For the first line:
#
#     Print each string in start1, capitalized and followed by an exclamation point and a space.
#
#     Print first, also capitalized and followed by an exclamation point.
#
# For the second line:
#
#     Print start2 and a space.
#
#     Print second and a period.
print("\n------ 7.11 ------")

start1 = ["fee", "fie", "foe"]
rhymes = [("flop", "get a mop"),
          ("fope", "turn the rope"),
          ("fa", "get your ma"),
          ("fudge", "call the judge"),
          ("fat", "pet the cat"),
          ("fog", "walk the dog"),
          ("fun", "say we're done")]
start2 = "Someone better"

for rhyme in rhymes:
    # First line
    print(f"{start1[0].capitalize()}! {start1[1].capitalize()}! {start1[2].capitalize()}! {rhyme[0].capitalize()}!")
    # Second Line
    print(f"{start2} {rhyme[1]} \n")
