#Program that reads integers from user until blank line. Display all negatives, followe by all of zeros, followed by positive numbers. Within group numbers are displayed in order they were entered:
negatives=[]
zeros=[]
positives=[]
line=input("Enter numbers: ")
while line!="":
    num=int(line)
    if num<0:
        negatives.append(num)
    elif num>0:
        positives.append(num)
    else:
        zeros.append(num)
    line=input("Enter numbers: ")
for n in negatives:
    print(n)
for n in positives:
    print(n)
for n in zeros:
    print(n)