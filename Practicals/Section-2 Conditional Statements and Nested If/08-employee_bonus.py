experience = int(input("Enter your experience in years: "))

if experience >= 1:
    salary = int(input("Enter your salary: "))
    if salary >= 50000:
        performance = int(input("Enter your performance score: "))
        if performance >= 90:
            bonus = salary * 20 / 100
            print("Bonus Rate: 20%")

        elif performance >= 75:
            bonus = salary * 10 / 100
            print("Bonus Rate: 10%")

        else:
            bonus = salary * 5 / 100
            print("Bonus Rate: 5%")

    else:

        performance = int(input("Enter your performance score: "))
        if performance >= 90:
            bonus = salary * 15 / 100
            print("Bonus Rate: 15%")

        else:
            bonus = salary * 5 / 100
            print("Bonus Rate: 5%")

    print("Bonus Amount:", bonus)

else:
    print("You are not eligible for bonus")