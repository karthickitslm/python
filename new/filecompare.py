# Coding to compare 2 Text Files and Identify the Similarity
# Reading File1 in order to compare
x1 = open("D:/Coding/python1/python/new/text1.txt")
# Reading File2 in order to compare
x2 = open("D:/Coding/python1/python/new/text2.txt")

# Assigning Variable Values in order to compute the Task
x1_data = x1.readlines()
x2_data = x2.readlines()

i = 0

# Creating Iteration to read the file entries line by line
for line1 in x1_data:
    i += 1

    for line2 in x2_data:

        if line1 == line2:
           print("Line ", i, ": SAME")
        else: 
           print("Line ", i, ":")
        break

# Close Files

x1.close()
x2.close()