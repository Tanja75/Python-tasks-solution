#Integer n is perfect when the sum of all of the proper divisors of n is equal to n (28=1+2+4+7+14)
#Funcion that determines whether or not a positive integer is perfect:
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(6))