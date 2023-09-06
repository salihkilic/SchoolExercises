# Things to do, chapter 6
# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch06.html#idm45795014289432

# 6.1 Use a for loop to print the values of the list [3, 2, 1, 0].
print("\n------ 6.1 ------")
my_list = [3, 2, 1, 0]

for x in my_list:
    print(x)


# 6.2 Assign the value 7 to the variable guess_me, and the value 1 to the variable number. Write a while loop that
# compares number with guess_me. Print 'too low' if number is less than guess me. If number equals guess_me,
# print 'found it!' and then exit the loop. If number is greater than guess_me, print 'oops' and then exit the loop.
# Increment number at the end of the loop.
print("\n------ 6.2 ------")
guess_me = 7
number = 1

success = False
while not success:
    if number == guess_me:
        print("Found it!")
        # By setting success here, the while loop will stop because the condition (We have not succeeded in finding
        # the correct number, fails). You could also use the keyword "break" to achieve the same goal.
        success = True
    elif number < guess_me:
        print(f"Too low ---> Guess = {number} --- Target: {guess_me}")
        number += 1
    else:
        print("Whoooops, something went very wrong here!")


# 6.3 Assign the value 5 to the variable guess_me. Use a for loop to iterate a variable called number over range(10).
# If number is less than guess_me, print 'too low'. If it equals guess_me, print found it! and then break out of the
# for loop. If number is greater than guess_me, print 'oops' and then exit the loop.
print("\n------ 6.3 ------")
guess_me = 5

for number in range(10):
    if number == guess_me:
        print("Found it!")
        # If you don't use break here, you will continue guessing even though you found the answer.
        break
    elif number < guess_me:
        print(f"Too low ---> Guess = {number} --- Target: {guess_me}")
    else:
        print("Whoooops, something went very wrong here! You went past the correct number")
