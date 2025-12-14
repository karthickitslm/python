#Python Program which uses Multiple if conditions

score = input("Please Enter your Exam Score:")
mark = int(score)
if mark > 90:
    print("Congratulations!! Your Grade is A")
elif mark in range(80,89):
    print("You've Secured B Grade")
elif mark in range(70,79):
    print("You've Secured C Grade")
elif mark in range(60,69):
    print("You've Secured D Grade")    
else:
    print("You've secured F Grade")