# Things to do, chapter 22
import pandas

# 22.1 Install Pandas. Get the CSV file in Example 16-1. Run the program in Example 16-2. Experiment with some of the
# Pandas commands.
print("\n------ 20.1 ------")
data = pandas.read_csv('Files/villains.csv')

print("The whole dataset")
print(data)

print("\nOnly the first names:")
only_first_names = data['first']
print(only_first_names)

print("\nOnly a subsection (row 2 to 4) of the table: ")
specific_selection = data.iloc[2:5]
print(specific_selection)
