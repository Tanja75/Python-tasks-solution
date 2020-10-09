#Program that determnines if 3 strows of different lengths can form a triangle:
def triangle ():
    a=int(input("Enter the length of a: "))
    b=int(input("Enter the length of b: "))
    c=int(input("Enter the length of c: "))

    if (a+c>c) and (b+c>a) and (a+c>b):
        print("Yes")
    else:
        print("No")
triangle()