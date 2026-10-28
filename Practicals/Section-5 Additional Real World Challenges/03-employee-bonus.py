# Employee Bonus 
# Conditions: 
# - Experience >= 1 year and salary >= ₹50,000: 
# - Performance >= 90 -> 20% bonus 
# - Performance >= 75 -> 10% bonus 
# - Otherwise -> 5% bonus 
# - Salary < ₹50,000: 
# - Performance >= 90 -> 15% bonus 
# - Otherwise -> 5% bonus

experience = int(input("Enter Experience in Years: "))
salary = float(input("Enter Salary: "))
performance = int(input("Enter Performance Score: "))

if experience >= 1 and salary >= 50000:
    if performance >= 90:
        bonus = salary * 20 / 100
    elif performance >= 75:
        bonus = salary * 10 / 100
    else:
        bonus = salary * 5 / 100

elif salary < 50000:
    if performance >= 90:
        bonus = salary * 15 / 100
    else:
        bonus = salary * 5 / 100

else:
    bonus = 0

print("Employee Bonus: ₹", bonus)
print("Total Salary: ₹", salary + bonus)