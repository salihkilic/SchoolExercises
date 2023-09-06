# Things to do, chapter 4
# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch04.html#idm45795036770920

# 4.1 Choose a number between 1 and 10 and assign it to the variable secret. Then, select another number between 1
# and 10 and assign it to the variable guess. Next, write the conditional tests (if, else, and elif) to print the
# string 'too low' if guess is less than secret, 'too high' if greater than secret, and 'just right' if equal to secret.
from random import randint, choice

print("\n------ 4.1 ------")
# Randint *includes* both arguments
secret = randint(1,10)
guess = randint(1,10)

success = False
while not success:
    if guess == secret:
        # Set success to true, so we can escape the wile loop
        success = True
        print("Just right")

    elif guess < secret:
        print(f"Too low: {guess} is lower than {secret}")
        guess = randint(1, 10)

    else:
        print(f"Too high {guess} is higher than {secret}")
        guess = randint(1, 10)


# 4.2 Assign True or False to the variables small and green. Write some if/else statements to print which of these
# matches those choices: cherry, pea, watermelon, pumpkin.
print("\n------ 4.2 ------")
# This picks random boolean values for each category on every run
IsSmall = choice([True, False])
IsGreen = choice([True, False])

# Let's put this in a Tuple for easy comparison
random_picks = (IsSmall, IsGreen)

print(f"We picked: \n"
      f"Small: {IsSmall} \n"
      f"Green: {IsGreen} \n")

# The tuples are set as (Is Small, Is Green). A watermelon is NOT Small (false), but IS green (True).
cherry = (True, False)
pea = (True, True)
watermelon = (False, True)
pumpkin = (False, False)

# This could be done more concise but the exercise wants us to use if/else statements
if cherry == random_picks:
    print("Cherry matches")
else:
    print("Cherry does not match")

if pea == random_picks:
    print("Pea matches")
else:
    print("Pea does not match")

if watermelon == random_picks:
    print("Watermelon matches")
else:
    print("Watermelon does not match")

if pumpkin == random_picks:
    print("Pumpkin matches")
else:
    print("Pumpkin does not match")