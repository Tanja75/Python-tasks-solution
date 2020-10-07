#Program that reads integers from the user and stores them in the list until the user enters 0 then display all the values (except 0) from smallest to largest:
data=[]
num=int(input("Enter an integer: "))
while num !=0:
    data.append(num)
    num=int(input("Enter an integer: "))
data.sort(reverse=True)
print("the numbers in descending order are: ")
for num in data:
    print(num)