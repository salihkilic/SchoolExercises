from array import array


def insertion_sort(a: array):
    print(f"Starting Array: {a.tolist()}")
    n = len(a)
    i = 1
    while i < n:
        current = a[i]
        j = i - 1
        while j >= 0 and a[j] > current:
            print(f"Inserting {current} to the left, because: {current} < {a[j]}")
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = current
        print(f"{current} sorted, updated array: {a.tolist()}")
        i = i + 1


if __name__ == '__main__':
    test_array = array('i', [11, 5, 7, 4, 8, 2, 12])
    insertion_sort(test_array)
