#Program that generates a random selection og 6 numbers for a lotary ticket and doesn't containe duplicates. Display in asc order:
from random import shuffle
lottery=list(range(1,60))
numbers=[]

for i in range(6):
    shuffle(lottery)
    x=lottery.pop()
    numbers.append(x)

numbers.sort()
print("Your numbers are: ", numbers)
