# find the sum of odd numbers from 1 to 100
total = 0
for i in range(1, 101):
    if i % 2 != 0:
        total += i
print("The sum of odd numbers from 1 to 100 is:", total)

# output: The sum of odd numbers from 1 to 100 is: 2500