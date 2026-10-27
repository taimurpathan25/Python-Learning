# create a login system with role-based access control

# Conditions: 
# - Check username. 
# - If username is correct, check password. 
# - If password is correct, check role: 
# - "admin" -> Full Access 
# - "teacher" -> Teacher Dashboard 
# - "student" -> Student Dashboard 
# - Anything else -> Invalid Role 
# - Wrong password -> "Wrong Password" 
# - Wrong username -> "Invalid Username" 

valid_username = "user123"
valid_password = "pass@123"
valid_role = "student"

input_username = input("Enter your username: ")
if input_username == valid_username:
    input_password = input("Enter your password: ")
    if input_password == valid_password:
        input_role = input("Enter your role (admin/teacher/student): ")
        if input_role == "admin":
            print("Welcome Admin! You have full access.")
        elif input_role == "teacher":
            print("Welcome Teacher! You have access to the Teacher Dashboard.")
        elif input_role == "student":
            print("Welcome Student! You have access to the Student Dashboard.")
        else:
            print("Invalid Role")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")