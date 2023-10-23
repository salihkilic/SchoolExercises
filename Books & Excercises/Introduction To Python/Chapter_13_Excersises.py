# Things to do, chapter 13
# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch13.html#idm45794985381672

from datetime import date, timedelta
from random import randint

# 13.1 Write the current date as a string to the text file today.txt.
print("\n------ 13.1 ------")

# I'm a bit confused. Reading and writing files is the next chapter, but we are supposed to be able to do this exercise.
# You can find today.txt in the "Files" folder.
with open("Files/today.txt", 'wt') as fwrite:
    fwrite.write(date.today().__str__())

print(f"Check Files/today.txt for contents, it should say {date.today()}")

# 13.2 Read the text file today.txt into the string today_string.
print("\n------ 13.2 ------")
with open("Files/today.txt", 'rt') as fread:
    today_string = fread.readline()
    print(today_string)

# 13.3 Parse the date from today_string.
print("\n------ 13.3 ------")
year, month, day = today_string.split("-")

print(f"We extracted the following data:\n"
      f"Year: {year}\n"
      f"Month: {month}\n"
      f"Day: {day}\n")

date_from_today_string = date(int(year), int(month), int(day))
print(f"The date: {date_from_today_string}")

# 13.4 Create a date object of your day of birth.
print("\n------ 13.4 ------")
# Well, I'm not trying to post my personal information on the internet, so let's create some random values.
# To make this as easy as possible, let's just assume we don't get born after the 28th of any given month.
year = randint(1970, 2000)
month = randint(1, 12)
day = randint(1, 28)

print(f"We created the following random numbers:\n"
      f"Year: {year}\n"
      f"Month: {month} \n"
      f"Day: {day} \n")

date_object = date(year, month, day)
print(f"Which created the following date object: {date_object}")

# 13.5 What day of the week was your day of birth?
print("\n------ 13.5 ------")

days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f"The day of the week for {date_object} is {days_of_the_week[date_object.weekday()]}")

# 13.6 When will you be (or when were you) 10,000 days old?
print("\n------ 13.6 ------")
date_at_10k = date_object + timedelta(days=10000)

print(f"      We start at:     {date_object}\n"
      f"After 10.000 days:     {date_at_10k}")
