# Nested Dictionary - Employee Experience Classify employees based on salary and experience. 
# Conditions: 
# - Salary >= ₹50,000:  
# - Experience >= 5 years -> Senior 
# - Otherwise -> Mid-Level 
# - Salary < ₹50,000:   
# - Experience >= 3 years -> Experienced Junior  
# - Otherwise -> Fresher/Junior

employees = {
    "Rahul": {
        "salary": 60000,
        "experience": 6 
        },  
    "Amit": {
        "salary": 40000,
        "experience": 4
        },  
    "Priya": {
        "salary": 70000,
        "experience": 3
        },
    "Neha": {
        "salary": 45000,
        "experience": 2
        }
}

for name, info in employees.items():
    salary = info["salary"]
    experience = info["experience"]
    
    if salary >= 50000:
        if experience >= 5:
            category = "Senior"
        else:
            category = "Mid-Level"
    else:
        if experience >= 3:
            category = "Experienced Junior"
        else:
            category = "Fresher/Junior"
    
    print(f"{name}: Salary: ₹{salary}, Experience: {experience} years - {category}")
    
    
# output:Rahul: Salary: ₹60000, Experience: 6 years - Senior
# Amit: Salary: ₹40000, Experience: 4 years - Experienced Junior
# Priya: Salary: ₹70000, Experience: 3 years - Mid-Level
# Neha: Salary: ₹45000, Experience: 2 years - Fresher/Junior