# Replace negative numbers with 0 and store the result in a new list. 
 
numbers = [10, -5, 20, -8, 30, -2] 
result = [num if num >= 0 else 0 for num in numbers]
print(result)


# output:
# [10, 0, 20, 0, 30, 0]