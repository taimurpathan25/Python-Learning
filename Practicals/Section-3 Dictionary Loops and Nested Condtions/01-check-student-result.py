# check student result based on marks obtained.
# conditions:
# - If marks >= 40: Pass
# - If marks < 40: Fail

# Data: 
# students = { 
# "Rahul": 75,         
# "Amit": 32,         
# "Priya": 88,         
# "Neha": 39,         
# "Rohit": 55     
# } 

students = {
    "Rahul": 75,
    "Amit": 32,
    "Priya": 88,
    "Neha": 39,
    "Rohit": 55
}

print("------- Student Results -------")

for student, marks in students.items():
    if marks >= 40:
        result = "Pass"
    else:
        result = "Fail"
    print(f"{student} has {result} with {marks} marks.")
    
    
    
# output:
# ------- Student Results -------
# Rahul has Pass with 75 marks.
# Amit has Fail with 32 marks.
# Priya has Pass with 88 marks.
# Neha has Fail with 39 marks.
# Rohit has Pass with 55 marks.