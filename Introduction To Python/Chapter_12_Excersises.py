# Things to do, chapter 12
import binascii

import unicodedata
import re
import struct

# 12.1 Create a Unicode string called mystery and assign it the value '\U0001f984'. Print mystery and its Unicode name.
print("\n------ 12.1 ------")
# Please note the import statement at the top of the file
mystery = '\U0001f984'
print(mystery)
print(unicodedata.name(mystery))

# 12.2 Encode mystery, this time using UTF-8, into the bytes variable pop_bytes. Print pop_bytes.
print("\n------ 12.2 ------")
pop_bytes = mystery.encode("UTF-8")
print(pop_bytes)

# 12.3 Using UTF-8, decode pop_bytes into the string variable pop_string. Print pop_string. Is pop_string equal to
# mystery?
print("\n------ 12.3 ------")
pop_string = pop_bytes.decode("UTF-8")
print(f"pop_string: {pop_string}")
print(f"mystery: {mystery}")
print(f"Are they the same thing?: {mystery == pop_string}")

# 12.4 When you’re working with text, regular expressions come in very handy. We’ll apply them in a number of ways to
# our featured text sample. It’s a poem titled “Ode on the Mammoth Cheese,” written by James McIntyre in 1866 in
# homage to a seven-thousand-pound cheese that was crafted in Ontario and sent on an international tour. If you’d
# rather not type all of it, use your favorite search engine and cut and paste the words into your Python program,
# or just grab it from Project Gutenberg. Call the text string mammoth. Example 12-1. mammoth.txt
#
print("\n------ 12.4 ------")

mammoth = "We have seen thee, queen of cheese," \
          "Lying quietly at your ease,\n" \
          "Gently fanned by evening breeze,\n" \
          "Thy fair form no flies dare seize.\n" \
          "All gaily dressed soon you'll go\n" \
          "To the great Provincial show,\n" \
          "To be admired by many a beau\n" \
          "In the city of Toronto.\n\n" \
          "Cows numerous as a swarm of bees,\n" \
          "Or as the leaves upon the trees,\n" \
          "It did require to make thee please,\n" \
          "And stand unrivalled, queen of cheese.\n\n" \
          "May you not receive a scar as\n" \
          "We have heard that Mr. Harris\n" \
          "Intends to send you off as far as\n" \
          "The great world's show at Paris.\n\n" \
          "Of the youth beware of these,\n" \
          "For some of them might rudely squeeze\n" \
          "And bite your cheek, then songs or glees\n" \
          "We could not sing, oh! queen of cheese.\n\n" \
          "We'rt thou suspended from balloon,\n" \
          "You'd cast a shade even at noon,\n" \
          "Folks would think it was the moon\n" \
          "About to fall and crush them soon.\n"
print(mammoth)


# 12.5 Import the re module to use Python’s regular expression functions. Use the re.findall() to print all the words
# that begin with c.
print("\n------ 12.5 ------")

# If you've never done regular expressions, may the odds be ever in your favour. They're black magic to me.
# Explanation of the following regex:
# \b means "Any word starting with"
# [cC] means "c OR C"
# \w* means any amount of word characters
# Together this means: "Look for any word starting with c or C, with any amount of letters after that (but not a space)"
print(re.findall(r'\b[cC]\w*', mammoth))


# 12.6 Find all four-letter words that begin with c.
print("\n------ 12.6 ------")
# Similar to the one above, but with the addition of \w{3}, which set a limit of 3 letters after the initial c or C,
# for a total of four letters, instead of the "any" amount we set in the previous exercise.
print(re.findall(r'\b[cC]\w{3}\b', mammoth))


# 12.7 Find all the words that end with r.
print("\n------ 12.7 ------")
# In short: \b(word boundary) \w*(any amount of letters) [r](only the letter r) \b(word boundary)
print(re.findall(r'\b\w*r\b', mammoth))


# 12.8 Find all words that contain exactly three vowels in a row.
print("\n------ 12.8 ------")
# You should be able to understand this, following the instructions above
print(re.findall(r'\b\w*[aeiouy][aeiouy][aeiouy]\w*\b', mammoth))


# 12.9 Use unhexlify to convert this hex string (combined from two strings to fit on a page) to a bytes variable
# called gif:
print("\n------ 12.9 ------")

hex_string = b'47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b'
gif = binascii.unhexlify(hex_string)
print(gif)

# 12.10 The bytes in gif define a one-pixel transparent GIF file, one of the most common graphics file formats. A
# legal GIF starts with the ASCII characters GIF89a. Does gif match this?
print("\n------ 12.10 ------")

legal_gif_bytestring = b'GIF89a'
print(f"gif variable is a legal GIF: {gif[0:6] == legal_gif_bytestring}")


# 12.11 The pixel width of a GIF is a 16-bit little-endian integer beginning at byte offset 6, and the height is the
# same size, starting at offset 8. Extract and print these values for gif. Are they both 1?
print("\n------ 12.11 ------")

# I'm actually not absolutely sure this is correct. Because width starts at offset 6 and height starts at 8,
# I assume we're looking for a short integer. Short integers are 2 bytes compared to integers (4 bytes).
#
width = struct.unpack_from("<h", gif, 6)
height = struct.unpack_from("<h", gif, 8)

print(f"Width: {width[0]}")
print(f"Height: {height[0]}")
print(f"Width is same as height: {width == height}")
