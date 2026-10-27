# Student Marks and Attendance The following dictionary contains students' marks and attendance. 
# Conditions: 
# - If attendance < 75 -> Not Eligible 
# - If attendance >= 75:   
# - Marks >= 80 -> Distinction  
# - Marks >= 60 -> First Division  
# - Marks >= 40 -> Pass 
# - Marks < 40 -> Fail 

students = {
    "Rahul": {
        "marks": 85, 
        "attendance": 90
        },         
    "Amit": {
        "marks": 35,
        "attendance": 80
        },
    "Priya": {
        "marks": 65,
        "attendance": 70
        },
    "Neha": {
        "marks": 45,
        "attendance": 85
        },
    "Rohit": {
        "marks": 90,
        "attendance": 60
        }
}

for student, info in students.items():
    marks = info["marks"]
    attendance = info["attendance"]
    
    if attendance < 75:
        eligibility = "Not Eligible"
    else:
        if marks >= 80:
            eligibility = "Distinction"
        elif marks >= 60:
            eligibility = "First Division"
        elif marks >= 40:
            eligibility = "Pass"
        else:
            eligibility = "Fail"
    
    print(f"{student}: Marks: {marks}, Attendance: {attendance}% - {eligibility}")
    
    
    
# output:
# Rahul: Marks: 85, Attendance: 90% - Distinction
# Amit: Marks: 35, Attendance: 80% - Fail
# Priya: Marks: 65, Attendance: 70% - Not Eligible
# Neha: Marks: 45, Attendance: 85% - Pass
# Rohit: Marks: 90, Attendance: 60% - Not Eligible