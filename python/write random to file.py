import random

with open("mike.txt", "w") as outfile:
    for i in range(5000):
        number = random.randint(1, 500)
        print(number)
        outfile.write(str(number) + "\n")


