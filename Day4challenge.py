number= (input("Enter a Number for which the multiplication table to be generated"))
x = input("Enter the range of the multiplication")
y = int(x)
z = int(number)
for i in range(1, y+1):
    print(f"{number} X {i} = {i * z}")
