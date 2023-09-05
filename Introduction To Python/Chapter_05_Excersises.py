# Things to do, chapter 5

# 5.1 Capitalize the word starting with m:
print("\n------ 5.1 ------")

song = "When an eel grabs your arm, And it causes great harm, That's - a moray!"
print(f"Original text: {song}")

better_song = song.replace("m", "M")
print(f"New text: {better_song}")


# 5.2 Print each list question with its correctly matching answer, in the form:
#      Q: question
#      A: answer
print("\n------ 5.2 ------")

questions = ["We don't serve strings around here. Are you a string?",
             "What is said on Father's Day in the forest?",
             "What makes the sound 'Sis! Boom! Bah!'?"]

answers = ["An exploding sheep.",
           "No, I'm a frayed knot.",
           "'Pop!' goes the weasel."]

print(f"Q: {questions[0]} \n"
      f"A: {answers[1]} \n")

print(f"Q: {questions[1]} \n"
      f"A: {answers[2]} \n")

print(f"Q: {questions[2]} \n"
      f"A: {answers[0]} \n")

# 5.3 Write the following poem by using old-style formatting. Substitute the strings 'roast beef', 'ham', 'head',
# and 'clam' into this string:
#
# My kitty cat likes %s,
# My kitty cat likes %s,
# My kitty cat fell on his %s
# And now thinks he's a %s.
print("\n------ 5.3 ------")

print("My kitty cat likes %s" % "roast beef")
print("My kitty cat likes %s" % "ham")
print("My kitty cat fell on his %s" % "head")
print("And now thinks he's a %s" % "clam")


# 5.4 Write a form letter by using new-style formatting. Save the following string as letter (you’ll use it in the
# next exercise):
print("\n------ 5.4 ------")
letter = "Dear {salutation} {name},\n\n"\
         "Thank you for your letter. We are sorry that our {product}\n"\
         "{verbed} in your {room}. Please note that it should never\n"\
         "be used in a {room}, especially near any {animals}.\n\n"\
         "Send us your receipt and {amount} for shipping and handling.\n"\
         "We will send you another {product} that, in our tests,\n"\
         "is {percent}% less likely to have {verbed}.\n\n"\
         "Thank you for your support.\n\n"\
         "Sincerely,\n"\
         "{spokesman}\n"\
         "{job_title}\n"


# 5.5 Assign values to variable strings named 'salutation', 'name', 'product', 'verbed' (past tense verb), 'room',
# 'animals', 'percent', 'spokesman', and 'job_title'. Print letter with these values, using letter.format().
print("\n------ 5.5 ------")

print(letter.format(salutation="Mr.",
                    name="Peter",
                    product="smoke machine",
                    verbed="broke down",
                    room="bedroom",
                    animals="lamas",
                    amount="a million dollars",
                    percent="0.75",
                    spokesman="Eric Smog",
                    job_title="Customer Relations"
                    ))

# 5.6 After public polls to name things, a pattern emerged: an English submarine (Boaty McBoatface), an Australian
# racehorse (Horsey McHorseface), and a Swedish train (Trainy McTrainface). Use % formatting to print the winning
# name at the state fair for a prize duck, gourd, and spitz.
print("\n------ 5.6 ------")

old_style_format_string = "%sy Mc%sface"
horse = "Horse"
gourd = "Gourd"
spitz = "Spitz"

print("Winners (Old style format):")
print(old_style_format_string % (horse, horse))
print(old_style_format_string % (gourd, gourd))
print(old_style_format_string % (spitz, spitz))

# 5.7 Do the same, with format() formatting.
print("\n------ 5.7 ------")
new_style_format_string = "{0}sy Mc{0}face"

print("Winners (New style format):")
print(new_style_format_string.format(horse))
print(new_style_format_string.format(gourd))
print(new_style_format_string.format(spitz))

# 5.8 Once more, with feeling, and f strings.
print("\n------ 5.8 ------")

print("Winners (With f-strings):")
print(f"{horse}sy Mc{horse}face")
print(f"{gourd}sy Mc{gourd}face")
print(f"{spitz}sy Mc{spitz}face")
