#Program that reads the number of containers of each size (liter or more than liter) from user and computes and displays the refund (0.10$ for 1 liter and 0.25$ for more than 1 liter)
liter=float(input("Enter the number of 1 l bottles :"))
smaller=float(input("Enter the number of bootles bigger than 1 l: "))

number=liter*0.25+smaller*0.10
print("The amount of refund is: ", number, "$")