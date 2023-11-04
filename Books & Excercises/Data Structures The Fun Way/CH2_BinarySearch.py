import random
from math import floor


def binary_search(a: list, target: int):
    index_high = len(a) - 1
    index_low = 0

    while index_low <= index_high:
        index_midpoint = floor((index_high + index_low) / 2)

        if a[index_midpoint] == target:
            print(f"Found target! Target: ({target}) -- Location: {index_midpoint}")
            return index_midpoint

        if a[index_midpoint] < target:
            index_low = index_midpoint + 1
            print(
                f"Target ({target}) is higher "
                f"than midpoint -- Setting lower bound to {index_low}")

        elif a[index_midpoint] > target:
            index_high = index_midpoint - 1
            print(f"Target ({target}) is lower "
                  f"than midpoint -- Setting upper bound to {index_high}")

        else:
            print("Something went wrong at:\n"
                  f"Low: {index_low} -- {a[index_low]}\n"
                  f"High: {index_high} -- {a[index_high]}\n"
                  f"Mid: {index_midpoint} -- {a[index_midpoint]}\n"
                  f"Target: {target}")
            print(f"{a} \n")
    print("Could not find target in list. Stopping search.")
    return False


if __name__ == '__main__':

    integer_list = []
    for x in range(100000):
        integer_list.append(random.randint(1, 100_000))

    target = random.choice(integer_list)
    integer_list.sort()

    binary_search(integer_list, target)
