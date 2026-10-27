# Find names starting with "A" and store them in a new list. 
names = ["Amit", "Rahul", "Ankit", "Neha", "Arjun", "Rohit"] 
starting_with_A = [name for name in names if name.startswith("A")]
print(starting_with_A)

# output:
# ['Amit', 'Ankit', 'Arjun']