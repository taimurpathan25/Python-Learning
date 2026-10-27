# Find names having more than 4 characters and store them in a new list

names = ["Amit", "Rahul", "Neha", "Rohit", "Sneha"] 
more_than_4_chars = [name for name in names if len(name) > 4]
print(more_than_4_chars)

# output:
# ['Rahul', 'Rohit', 'Sneha']