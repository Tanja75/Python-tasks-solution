#Function to find the max of 3 numbers:
def max_of_two (x,y):
    if x>y:
        return x
    return y
def max_of_three(x,y,z):
    return max_of_two(x, max_of_two(y,z))
print(max_of_three(58,6,19))