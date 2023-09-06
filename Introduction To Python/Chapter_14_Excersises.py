# Things to do, chapter 14
# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch14.html#idm45794982012168

import os

# 14.1 List the files in your current directory.
print("\n------ 14.1 ------")
item_list = os.listdir('.')

# Filter out folders"
file_list = [file for file in item_list if "." in file]
for file in file_list:
    print(file)

# 14.2 List the files in your parent directory.
print("\n------ 14.2 ------")
file_list = os.listdir('..')
for file in file_list:
    print(file)

# 14.3 Assign the string 'This is a test of the emergency text system' to the variable test1, and write test1 to a
# file called test.txt.
print("\n------ 14.3 ------")
test1 = "This is a test of the emergency text system"

with open("Files/test.txt", 'wt') as writer:
    writer.write(test1)

print(f"Check Files/test.txt for contents, it should say '{test1}'")

# 14.4 Open the file test.txt and read its contents into the string test2. Are test1 and test2 the same?
print("\n------ 14.4 ------")

with open("Files/test.txt", 'rt') as reader:
    test2 = reader.read()

print(f"We read: {test2}")
print(f"Test1 and Test2 variables are the same: {test1 == test2}")
