# Python Program to Do Simple Math calcultion
# Asking the User to feed 2 numbers
num1 = input("Please enter the 1st Number")
# Handling Exception using Try and Except
try:
    x = int(num1)
except ValueError:
    print("That's not a number")    
num2 = input("Please enter the 2nd Number")
try:
    y = int(num2)
except ValueError:
    print("That's not a number")  
#converting integer to float
n1 = float(num1)
n2 = float(num2)
# Adding Numbers
plus = n1 + n2
# Subtracting Numbers
difference = n1 - n2
# Multiplying Numbers
multi = n1 * n2
# Dividing Numbers
div = n1 / n2

print("The Sum of 2 numbers is", plus)
print("The Subtraction value of 2 numbers is", difference)
print("The Multiplication value of 2 numbers is", multi)
print("The Division of 2 numbers is", div)
