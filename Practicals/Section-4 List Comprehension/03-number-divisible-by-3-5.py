#  Find numbers divisible by both 3 and 5 and store them in a new list. 

numbers = [10, 15, 20, 30, 45, 50, 60, 75] 
divisible_by_3_and_5 = [num for num in numbers if num % 3 == 0 and num % 5 == 0]
print(divisible_by_3_and_5)

# output:
# [15, 30, 45, 60, 75]