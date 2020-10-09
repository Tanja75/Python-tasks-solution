#Program reads the integer from user and displays whether the numer is even or odd:
input_1=input("Enter integer: ")
number=int(input_1)
if number %2==0:
    print("The number is even")
else:
    print("The number is odd")