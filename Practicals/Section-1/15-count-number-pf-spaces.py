# Count the number of Spaces in String 

# text = "Python is Easy to Learn"
# count = text.count(" ")
# print("Number of Spaces in given String is : ", count)


#output :
# Number of Spaces in given String is :  4.


text = "Python is easy to Learn"
count = 0
for char in text:
    if char == " ":
        count += 1
print("The number of spaces in the String is : ", count)


# output:
# The number of spaces in the String is :  4