#Program that takes a list and returns unique elements:
def unique(l):
    x=[]
    for a in l:
        if a is not x:
            x.append(a)
    return x
print(unique([1,2,44,5,77,86,456,34]))