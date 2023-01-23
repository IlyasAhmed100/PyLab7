# Task 7.2

# Setting variables
raw_numbers = 1
odd_numbers = 0
even_numbers = 0

# Asking user to input integers
while raw_numbers != 0:
    raw_numbers = int(input("Please type in a series of integers and type 0 to stop:" '\n'))
# Checking odd numbers and even numbers
    if raw_numbers % 2 != 0:
        odd_numbers += 1
    elif raw_numbers % 2 == 0:
        even_numbers += 1

# Checking odd numbers and even numbers

# Printing out how many odd or even numbers there are

print("There are " + str(odd_numbers) + " odd numbers and " + str(even_numbers - 1) + " even numbers.")
    

                  
                  

