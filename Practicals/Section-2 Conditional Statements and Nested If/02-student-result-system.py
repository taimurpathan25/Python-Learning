# write a python program that takes the marks of 3 subjects.
subject1 = int(input("Enter the marks for subject 1: "))
subject2 = int(input("Enter the marks for subject 2: "))
subject3 = int(input("Enter the marks for subject 3: "))

total_marks = subject1 + subject2 + subject3
average_marks = total_marks / 3
if subject1 >= 40 and subject2 >= 40 and subject3 >= 40:
    print("Percentage : ", average_marks)
    if average_marks >= 75:
        print("Distinction")
    elif average_marks >= 60:
        print("First Division")
    elif average_marks >= 50:
        print("Second Division")
    else:
        print("Pass");
else:
    print("Fail")



# output:
# Enter the marks for subject 1: 75
# Enter the marks for subject 2: 85
# Enter the marks for subject 3: 95
# Percentage :  85.0
# Distinction