# Things to do, chapter 9

# 9.1 Define a function called good() that returns the following list: ['Harry', 'Ron', 'Hermione'].
print("\n------ 9.1 ------")


def good():
    return ['Harry', 'Ron', 'Hermione']


print(good())

# 9.2 Define a generator function called get_odds() that returns the odd numbers from range(10). Use a for loop to
# find and print the third value returned.
print("\n------ 9.2 ------")


def get_odds():
    for item in range(10):
        if item % 2 == 1:
            yield item


item_count = 0
for x in get_odds():
    item_count += 1
    if item_count == 3:
        print(f"{x} is the third odd number")

# 9.3 Define a decorator called test that prints 'start' when a function is called, and 'end' when it finishes.
print("\n------ 9.3 ------")


def function_decorator(func):
    print("Start")
    func()
    print("End")


@function_decorator
def decorated_function():
    print("The main function")


# 9.4 Define an exception called OopsException. Raise this exception to see what happens. Then, write the code to
# catch this exception and print 'Caught an oops'.
print("\n------ 9.4 ------")


class OopsException(Exception):
    pass


try:
    raise OopsException("Uh oh")
except OopsException as exc:
    print(f"I caught an oops: {exc}")
