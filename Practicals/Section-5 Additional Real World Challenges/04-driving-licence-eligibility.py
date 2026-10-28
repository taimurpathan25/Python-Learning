# Driving License Eligibility 
# Conditions: 
# - Age >= 18. 
# - Learner license must be available. 
# - Driving test score >= 60. 

age = int(input("Enter your age: "))
learner = input("Do you have a learner license? (yes/no): ")
score = int(input("Enter driving test score: "))

if age < 18:
    print("Not Eligible: Age must be 18 or above.")
elif learner != "yes":
    print("Not Eligible: Learner license is required.")
elif score < 60:
    print("Not Eligible: Driving test score must be 60 or above.")
else:
    print("Eligible for Driving License!")