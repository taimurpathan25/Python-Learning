# Electricity Bill 
# Conditions: 
# - 0-100 units -> ₹5/unit 
# - 101-200 units -> ₹7/unit 
# - 201-300 units -> ₹10/unit 
# - Above 300 units -> ₹15/unit 
# - If the bill exceeds ₹3,000, add a 10% surcharge.


units = int(input("Enter Electricity Units Consumed: "))
if units < 0:
    print("Invalid Units !")
else:
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = units * 7
    elif units <= 300:
        bill = units * 10
    else:
        bill = units * 15
    
    if bill > 3000:
        bill = bill + (bill * 10 / 100)
    print("Total Electicity Bill : ₹",bill);   
    