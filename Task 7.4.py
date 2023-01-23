# Task 7.4

# Importing functions
import numpy as np

# Setting the number of coin flips to 10
total_coin_flips = 100000

# Setting an array to save coin flips into
coin_flips = np.ones(total_coin_flips) * -1
np.random.seed(0)

# Using the for loop
for i in range(total_coin_flips):
    coin_flips[i] = np.random.randint(0,2)
    np.random.seed(i)
print(coin_flips)

# Counting the number of 1's and 0's to work out how many heads and tails there are
heads = (coin_flips == 0).sum()
tails = (coin_flips == 1).sum()

# Printing the total number of heads and tails
print("There are " + str(heads) + " heads and there are " + str(tails) + " tails.")
