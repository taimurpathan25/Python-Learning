# Check Even/Odd Values Given a dictionary, check whether each value is even or odd. 
# Conditions: 
# - Even and greater than 20 -> Large Even
# - Even and <= 20 -> Even
# - Odd -> Odd

data = {  
    "a": 10,
    "b": 15,  
    "c": 25,
    "d": 30,  
    "e": 40   
} 

for key, value in data.items():
    if value % 2 == 0 and value > 20:
        result = "Large Even"
    elif value % 2 == 0 and value <= 20:
        result = "Even"
    else:
        result = "Odd"

    print(f"{key}: {result}")
    
# output:
# a: Even
# b: Odd
# c: Odd
# d: Large Even
# e: Large Even
