# Task 7.3

# Initalise variables
vowel_count = 0

# Asking user to input a string
raw_string = str(input("Please enter a string:" '\n'))

# Setting up for loop to identify vowels
for vowel in raw_string:
    if vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u":
        vowel_count += 1

# Printing out how many vowels there are
print("There are " + str(vowel_count) + " vowels in this string.")
