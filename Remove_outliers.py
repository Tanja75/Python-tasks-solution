#Function that takes a list of values and n as its parameters. Creates new copy of the list with n largest and n smallest elements removed:
def removeOutliers (data, num_outliers):
    retval=sorted(data)
    for i in range(num_outliers):
        retval.pop()
    for i in range(num_outliers):
        retval.pop(0)
    return retval
def main():
    values=[]
    s=input("Enter value (blank line to quit): ")
    while s != "":
        num=(s)
        values.append(num)
        s=input("Enter value: ")
    if len(values)<4:
        print("You didn't entered enough values")
    else:
        print("With the outliers removed",removeOutliers(values,2))
        print("The original data: ", values)
main()
