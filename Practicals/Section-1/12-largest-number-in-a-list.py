# find the largest number in a list
data = [22, 55, 12, 89, 34, 67]
largest = data[0]
for i in range(1, len(data)):
    if data[i] > largest:
        largest = data[i]
print("The largest number in the list is:", largest)


# output: The largest number in the list is: 89