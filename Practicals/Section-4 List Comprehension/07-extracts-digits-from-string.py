# Extract digits from a string and store the result in a new list. 

data = "Python123Programming456"
digits = [char for char in data if char.isdigit()]
print(digits)

# output:
# ['1', '2', '3', '4', '5', '6'] 