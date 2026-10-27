# count vowels in a string
text = "Python is easy to learn"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("The number of vowels in the string is:", count)

# output: The number of vowels in the string is: 7