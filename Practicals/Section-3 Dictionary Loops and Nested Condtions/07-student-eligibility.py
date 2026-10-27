# Student Eligibility The dictionary contains student attendance and marks. 
# conditions:
# - Attendance >= 75 and marks >= 40 -> Eligible 
# - Attendance >= 75 and marks < 40 -> Failed in Exam 
# - Attendance < 75 -> Not Eligible  

students = {
    "Rahul": {
        "attendance": 85, 
        "marks": 70
        },
    "Amit": {
        "attendance": 60,
        "marks": 80
        },
    "Priya": {
        "attendance": 90,
        "marks": 35
        },
    "Neha": {
        "attendance": 78,
        "marks": 55
        }
    }

for student, info in students.items():
    attendance = info["attendance"]
    marks = info["marks"]
    
    if attendance >= 75:
        if marks >= 40:
            eligibility = "Eligible"
        else:
            eligibility = "Failed in Exam"
    else:
        eligibility = "Not Eligible"
    
    print(f"{student}: Attendance: {attendance}%, Marks: {marks} - {eligibility}")
    
    
    
# output:
# Rahul: Attendance: 85%, Marks: 70 - Eligible
# Amit: Attendance: 60%, Marks: 80 - Not Eligible
# Priya: Attendance: 90%, Marks: 35 - Failed in Exam
# Neha: Attendance: 78%, Marks: 55 - Eligible
