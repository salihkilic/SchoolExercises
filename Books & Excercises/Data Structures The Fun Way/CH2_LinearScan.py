import random


def linear_scan(a: list, target: int):
    for current_index, _ in enumerate(a):
        if a[current_index] == target:
            return current_index
    return "The target doesn't seem to be in the list"


if __name__ == '__main__':

    # Create our data
    random_integers = []
    for x in range(15):
        random_integers.append(random.randint(1, 10_000))
    target_int = random.choice(random_integers)

    # Print our results
    print("Simple linear scan. Basically a for loop.")
    print(f"Our random list of integers (1 to 10.000): {random_integers}")
    print(f"Our target int: {target_int}")
    print(f"Our target in is at index {linear_scan(random_integers, target_int)} \n")
