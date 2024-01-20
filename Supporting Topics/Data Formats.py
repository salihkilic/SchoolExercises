# Perform a free (re-)search and explore the answers for the following questions: Digits in
# decimal numbers are 0-9. What are the digits in hexadecimal format? What are the digits in
# binary format?

# Used this as research:
# https://en.wikipedia.org/wiki/Hexadecimal
# https://docs.python.org/3/library/functions.html#hex
# Conclusion, hexadecimal is base16 and Python contains a built-in function to display it


# Using python to convert those numbers:
for x in range(0, 10):
    print(f"Number in base10: {x}")
    print(f"Number in base16: {hex(x)[2:].upper()}")
    print(f"Number in base2: {x:08b}\n")

# Convert (manually) the following decimal numbers to hexadecimal and binary: 8, 10, 15, 21, 32,
# 64, 256, 500, 512, 1000.
print("-----------------------------\n"
      "Converting Decimal numbers: ")
decimal_numbers = [8, 10, 15, 21, 32, 64, 256, 500, 512, 1000]

for x in decimal_numbers:
    print(f"Number in base10: {x}")
    print(f"Number in base16: {hex(x)[2:].upper()}")
    print(f"Number in base2: {x:08b}\n")

#     Use Python to:
# Convert the decimal number 45 into its binary representation.
print("-----------------------------")
print(f"Number 45 in base2: {45:08b}")

# Convert the binary number 1010101 into decimal form.
print("-----------------------------")
print(f"Converting binary 1010101 into decimal: {int('1010101', 2)}")

# Add the binary numbers 10111 and 1101 and express the result in binary.
print("-----------------------------")
bin1 = "10111"
bin2 = "1101"

int1 = int(bin1, 2)
int2 = int(bin2, 2)

sum_int = int1 + int2
sum_bin = bin(sum_int)[2:]
print(f"Adding 10111 and 1101: {sum_bin}")
# Convert the decimal number 255 into its hexadecimal representation.
print("-----------------------------")
print(f"Converting decimal 255 into hex: {hex(255)[2:].upper()}")

# Convert the hexadecimal number 2A into decimal form.
print("-----------------------------")
print(f"Convert hexadecimal 2A into decimal: {int('2A', 16)}")

# Add the hexadecimal numbers C4 and 3A and express the result in hexadecimal.
print("-----------------------------")
hex1 = "C4"
hex2 = "3A"

int1 = int(hex1, 16)
int2 = int(hex2, 16)

sum_int = int1 + int2
sum_hex = hex(sum_int)[2:].upper()
print(f"Add hexadecimal C4 and 3A and display in hexadecimal: {sum_hex}")

# Convert the binary number 1101 into decimal form.
print("-----------------------------")
print(f"Convert binary 1101 into decimal: {int('1101', 2)}")

# Convert the hexadecimal number F0 into decimal form.
print("-----------------------------")
print(f"Convert hexadecimal F0 into decimal: {int('F0', 16)}")

# Add the decimal numbers 123 and 456.
print("-----------------------------")
print(f"Add decimal 123 and 456: {123 + 456}")

# Convert the decimal number 157 into binary and then into hexadecimal.
print("-----------------------------")
decimal_number = 157
binary_number = bin(157)[2:]
print(f"Convert decimal 157 into binary: {binary_number}")
print(f"Then into hexadecimal: {hex(int(binary_number, 2))[2:].upper()}")

# Convert the binary number 11101101 into decimal and then into hexadecimal.
print("-----------------------------")
into_decimal = int('11101101', 2)
print(f"Convert binary 11101101 into decimal: {into_decimal}")
print(f"And then into hexadecimal: {hex(into_decimal)[2:]}")

# Convert the hexadecimal number AB4 into decimal and then into binary.
print("-----------------------------")
into_decimal2 = int('AB4', 16)
print(f"Convert hexadecimal AB4 into decimal: {into_decimal2}")
print(f"And then into binary: {bin(into_decimal2)[2:]}")

#     Real-life Applications:
"""
Research and identify a real-world example where binary data is used extensively.
Source: https://en.wikipedia.org/wiki/Computer#Digital_computers
    - Binary is used in (almost) all digital computers. On the most basic level, transistors
      are either on or off, expressed through a 1 or a 0.
    - Same goes for its storage. Files are expressed in long sequences of binary data.
    
Source: https://www.zebra.com/us/en/resource-library/faq/what-is-barcode-symbology.html
    - Another interesting application (that I didn't know of!) is barcodes.
"""

"""
Investigate how hexadecimal is used in computer memory addressing.
Source: https://www.techtarget.com/whatis/definition/hexadecimal
I'm getting the impression that one of the biggest reasons we use hexadecimal in memory addressing
is because it's simply easier to read for humans and also more compact than binary. 
It's also simpler to understand. Beyond that, I didn't find any *technical* reasons why
we would use hexadecimal so much in memory adressing.

Source: https://www.researchgate.net/post/Why_we_are_using_HEXADECIMAL_values_for_computer_addressing
Maybe ONE reason, is that hexadecimal maps easily into binary because a single hexadecimal
character translates to four bits.
"""

"""
Explore how decimal data formats are used in financial calculations or accounting systems.

Source: https://en.wikipedia.org/wiki/Decimal

Not exactly sure what this question entails, but I'll do my best. Base10 is an excellent
human-readable format, simply because we have 10 fingers. There is one downside to it though.

Source: https://www.youtube.com/watch?v=PZRI1IfStY0

Floating point numbers in the decimal system don't have full representation in the binary system.
This is because these numbers are stored (in binary) in fractions of 2:

- 1
- 0.5
- 0.25
- 0.125
- etc...

The problem becomes then that when you try to express a number like 0.3, you can't do it precisely.
This is a non-trivial problem in financial calculations using digital systems. 
One solution (in financial systems) is to use a different base, like cents instead of 
euros and dividing by 100 at the end.
"""