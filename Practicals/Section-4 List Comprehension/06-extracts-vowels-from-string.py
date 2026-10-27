# Extract vowels from a string and store the result in a new list. 
text = "programming"
vowels = [char for char in text if char in "aeiouAEIOU"]
print(vowels)

# output:
# ['o', 'a', 'i']