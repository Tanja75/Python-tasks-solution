#Program calculates tax and tip for a meal. Tip is 18% of the meal amount without the tax. The output:tax amount, tip amount and grand total:
cost=float(input("Enter the cost of meal: "))
tax=cost*0.05
tip=cost*0.18
total=cost+tip+tax
print("Tax is %.2f, tip is %.2f, making the total cost %.2f" % (tax, tip, total))