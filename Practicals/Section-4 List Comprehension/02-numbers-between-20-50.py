# Find numbers between 20 and 50 and store them in a new list. 

numbers = [10, 25, 35, 60, 45, 15, 50, 70]
between_20_and_50 = [num for num in numbers if 20 < num < 50]
print(between_20_and_50)

# output:
# [25, 35, 45]