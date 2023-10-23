import os
import sys
import json

'''
print all contacts in the following format:
======================================
Position: <position>
First name: <firstname>
Last name: <lastname>
Emails: <email_1>, <email_2>
Phone numbers: <number_1>, <number_2>
'''


def display(addressbook: list):
    for contact in addressbook:
        print(f"Position: {contact['id']} \n"
              f"First name: {contact['first_name']} \n"
              f"Last name: {contact['last_name']} \n"
              f"Emails: {', '.join(contact['emails'])} \n"
              f"Phone numbers {', '.join(contact['phone_numbers'])}")


'''
return list of contacts sorted by first_name or last_name [if blank then unsorted], direction [ASC (default)/DESC])
'''


def list_contacts(addressbook, sort_by='first_name', direction='ASC'):
    if direction == 'ASC':
        direction = False
    else:
        direction = True

    sorted_address_book = sorted(addressbook,
                                 key=lambda entry: entry[sort_by],
                                 reverse=direction)

    display(sorted_address_book)

    return sorted_address_book


'''
add new contact:
- first_name
- last_name
- emails = {}
- phone_numbers = {}
'''


def add_contact(addressbook):
    # We need to make the new id one higher than last one
    highest_id = max(entry['id'] for entry in addressbook)

    # Get inputs
    f_name = input("Firstname:")
    l_name = input("Lastname:")
    emails = input("Emails:")
    phone_numbers = input("Phone Numbers:")

    # Add to addressbook
    addressbook.append({
        'id': highest_id + 1,
        'first_name': f_name,
        'last_name': l_name,
        'emails': emails.split(','),
        'phone_numbers': phone_numbers.split(',')
    })
    print("Contact added to addressbook")


'''
remove contact by ID (integer)
'''


def remove_contact():
    # todo: implement this function
    pass


'''
merge duplicates (automated > same fullname [firstname & lastname])
'''


def merge_contacts():
    # todo: implement this function
    ...


'''
read_from_json
Do NOT change this function
'''


def read_from_json(filename) -> list:
    addressbook = list()
    # read file
    with open(os.path.join(sys.path[0], filename)) as outfile:
        json_data = json.load(outfile)
        # iterate over each line in data and call the add function
        for contact in json_data:
            addressbook.append(contact)

    return addressbook


'''
write_to_json
Do NOT change this function
'''


def write_to_json(filename, addressbook: list) -> None:
    json_object = json.dumps(addressbook, indent=4)

    with open(os.path.join(sys.path[0], filename), "w") as outfile:
        outfile.write(json_object)


def main(json_file):
    addressbook = read_from_json(json_file)

    print("""    [L] List contacts
    [A] Add contact
    [R] Remove contact
    [M] Merge contacts
    [Q] Quit program""")

    print(addressbook)
    pick = input("Pick your action:")

    match pick.lower():
        case "l":
            list_contacts(addressbook)
        case "a":
            add_contact(addressbook)
        case "r":
            pass
        case "m":
            pass
        case "q":
            pass
        case _:
            pass


if __name__ == "__main__":
    main('contacts.json')
