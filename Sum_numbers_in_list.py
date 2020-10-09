#Function that sums all numbers in a list:
def sum(numbers):
    total=0
    for x in numbers:
        total += x
    return total
print(sum((18,34,78,56,235)))