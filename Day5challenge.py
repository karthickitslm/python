count = 0
a = (input("Enter your Password: \n "))
count = count + 1
b = (input("Enter your Password once again: "))
count = count + 1
while a != b:
    a = (input(f"Enter your Password: {count + 1} \n "))
    count = count + 1
    b = (input(f"Enter your Password once again: {count + 1} "))
    if a == b:
     print(" Welcome to the System, your password has been set!!")
    break
    count = count + 1
    if count > 6:
       print("Access Denied")
    break