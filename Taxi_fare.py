#Taxi fare consist of base fare of $4.00 plus $0.25 for every 140 m traveled.Program calculates total fare based on distance traveled:
def calculate_fare():
    distance=float(input("Enter distance "))
    distance=distance*1000
    fare=4.00+((distance/1400)*0.25)
    return fare

def print_fare(fare):
    print("%0s%.2f" % ("fare is: ", fare))

def main():
    fare=calculate_fare()
    print_fare(fare)
main()