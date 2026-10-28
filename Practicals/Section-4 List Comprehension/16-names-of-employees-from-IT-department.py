 # Find names of employees from the IT department.


employees = [
    {"name": "Amit", "department": "IT"},
    {"name": "Rahul", "department": "HR"},
    {"name": "Neha", "department": "IT"},
    {"name": "Rohit", "department": "Sales"}
]   
it_employees = [employee["name"] for employee in employees if employee["department"] == "IT"]
print(f"Employees from the IT department: {it_employees}") 
