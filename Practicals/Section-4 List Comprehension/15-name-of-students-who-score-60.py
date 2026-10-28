# Find names of students who scored 60 or more.     
 
students = [
        {"name": "Amit", "marks": 75},
        {"name": "Rahul", "marks": 45}, 
        {"name": "Neha", "marks": 90},         
        {"name": "Rohit", "marks": 55}     
]
passed_students = [student["name"] for student in students if student["marks"] >= 60]
print(f"Students who scored 60 or more: {passed_students}") 


# output: 
# Students who scored 60 or more: ['Amit', 'Neha']