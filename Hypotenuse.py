#Program that takes length of shorter sides of right triangle and computes hypotenuse:
from math import sqrt
print("Input lengths of shorter triangle sides: ")
a=float(input("a: "))
b=float(input("b: "))
c=sqrt(a**2+b**2)
print("The length of the hypothenuse is ",c)