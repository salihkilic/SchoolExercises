def is_integer(unchecked: str) -> bool:

    edited_string = unchecked.strip()
    is_negative = False
    is_valid = True

    # Remove + or -
    if edited_string[0] == '+':
        edited_string = edited_string[1:]
    elif edited_string[0] == '-':
        edited_string = edited_string[1:]
        is_negative = True

    # Check for alpha chars
    for character in edited_string:
        if str.isalpha(character):
            is_valid = False
            edited_string = remove_non_integer(edited_string)
            break

    print(["Invalid Integer", "Valid Integer"][is_valid])

    if is_negative:
        print(f"-{edited_string}")
    else:
        print(edited_string)


def remove_non_integer(unchecked: str) -> int:
    clean_str = ''
    for character in unchecked:
        if str.isdigit(character):
            clean_str += character
    return int(clean_str)

if __name__ == '__main__':
    tests = ['10','2ab3','+2134','-5433','-897saasd21','84skjdhaqw8176ghjg21']
    for test in tests:
        is_integer(test)
