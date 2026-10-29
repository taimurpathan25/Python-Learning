 # Find employees who earn more than ₹60,000 and belong to IT.

employees = [
    {"name": "Amit", "department": "IT", "salary": 55000},
    {"name": "Rahul", "department": "HR", "salary": 70000},
    {"name": "Neha", "department": "IT", "salary": 80000},
    {"name": "Rohit", "department": "IT", "salary": 45000}
]
it_employees_earning_more = [employee["name"] for employee in employees if employee["department"] == "IT" and employee["salary"] > 60000]
print(f"Employees from IT earning more than ₹60,000: {it_employees_earning_more}")



# output:
# Employees from IT earning more than ₹60,000: ['Neha']