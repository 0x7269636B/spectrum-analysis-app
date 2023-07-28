#create random numbers for testing
import random

NUMBERS = 1_000_000

file = open("random.txt", "a")

for i in range(NUMBERS):
    file.write(str(i) + "," + str(random.randint(0, 1000)) + "\n")

file.close()