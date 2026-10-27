# find the smallest number in a list
data = [22, 55, 12, 89, 34, 67]
smallest = data[0]
for i in range(1, len(data)):
    if data[i] < smallest:
        smallest = data[i]
print("The smallest number in the list is:", smallest)


# output: The smallest number in the list is: 12