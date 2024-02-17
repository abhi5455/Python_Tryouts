# Discount Calculator
cost = float(input("Enter the Original Cost: "))
discount = int(input("Enter Discount % : "))
amount = cost-(cost*(discount/100))
print("Amount to be paid after discount is:", amount)
