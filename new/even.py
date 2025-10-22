#Program to finding out Even numbers from a list of numbers
#numbers = input("Enter list of numbers")


# Function to find Even numbers:
def find_even_number(x):
    even = []
    for n in x:
        if not n %2:
            even.append(n)
    return even
# Getting User Input
numbers = input("Enter numbers separated by spaces")
# Sorting the Strings
sortedlist = numbers.split()
print(sortedlist)

# Converting the strings into Integers and creating a list

finallist = list(map(int, sortedlist))
print(finallist)

# Finding the Even numbers using the function
evennumbers = find_even_number(finallist)
print("List of Even Numbers", evennumbers)