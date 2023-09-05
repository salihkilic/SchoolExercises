# Things to do, chapter 3


# 3.1 How many seconds are in an hour? Use the interactive interpreter as a calculator and multiply the number of
# seconds in a minute (60) by the number of minutes in an hour (also 60).
print("\n------ 3.1 ------")
print(f"In every hour there are {60 * 60} seconds")

# 3.2 Assign the result from the previous task (seconds in an hour) to a variable called seconds_per_hour.
print("\n------ 3.2 ------")
seconds_per_hour = 60 * 60
print(seconds_per_hour)

# 3.3 How many seconds are in a day? Use your seconds_per_hour variable.
print("\n------ 3.3 ------")
print(f"There are {seconds_per_hour * 24} seconds in a day")

# 3.4 Calculate seconds per day again, but this time save the result in a variable called seconds_per_day.
print("\n------ 3.4 ------")
seconds_per_day = seconds_per_hour * 24
print(seconds_per_day)

# 3.5 Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.
print("\n------ 3.5 ------")
fp_division = seconds_per_day / seconds_per_hour
print(fp_division)

# 3.6 Divide seconds_per_day by seconds_per_hour, using integer (//) division. Did this number agree with the
# floating-point value from the previous question, aside from the final .0?
print("\n------ 3.6 ------")
int_division = seconds_per_day // seconds_per_hour
print(int_division)
print(f"Floating Point division and Integer division produce "
      f"the same result (aside from decimal notation): {fp_division == int_division}")
