# Student Performance Category Program of each student based on marks obtained.
# Conditions:
# - If marks >= 80 : Excellent
# - If marks >= 60 : Good
# - If marks >= 40 : Average
# - If marks < 40 : Fail 

Students = {
    "Rahul": 85,
    "Amit": 35,
    "Priya": 72,
    "Neha": 48
}

print("------- Student Performance Categories -------")

for student, marks in Students.items():
    if marks >= 80:
        category = "Excellent"
    elif marks >= 60:
        category = "Good"
    elif marks >= 40:
        category = "Average"
    else:
        category = "Fail"

    print(f"{student}: {marks} - {category}")
    
    
# Output
# ------- Student Performance Categories -------
# Rahul: 85 - Excellent
# Amit: 35 - Fail
# Priya: 72 - Good
# Neha: 48 - Average
