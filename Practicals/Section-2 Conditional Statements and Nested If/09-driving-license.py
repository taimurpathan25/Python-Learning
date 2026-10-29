# create a program that checks if a person is eligible for a driving license based on their age, whether they have a learner's license, and their driving test score. The program should prompt the user for their age, whether they have a learner's license (yes/no), and their driving test score. It should then determine if the person is eligible for a driving license based on the following.
# conditions: 
# saying that age >=18
#  learners license available?
#  driving test score >= 60

age = int(input("Enter your age : "));
if age>=18:
    learners_license = input("Do your have a learners license? (yes/no) : ");
    if learners_license == "yes":
        score = int(input("Enter your Driving test score : "));
        if score >=60:
            print("You are eligible for a driving license");
        else:
            print("You are not eligible,\n Your driving test score is Low");
    else:
        print("You are not eligible,\n bcs, You don't have learners license");
else:
    print("You are not eligible ,\n bcs, Your age is less than 18");
    

# output:
# Enter your age : 25 
# Do your have a learners license? (yes/no) : yes
# Enter your Driving test score : 98
# You are eligible for a driving license