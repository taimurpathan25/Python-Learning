# write the  python program for ATM withdrawal.

correct_pin = 0000
balance = 50000

pin = int(input("Enter Your Pin : "))

if pin == correct_pin:
    amount = int(input("Enter the amount to withdraw: "))

    if amount % 100 == 0:
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful! Please collect your cash.")
            print("Current balance:", balance)
        else:
            print("Insufficient funds. Please try again.")
    else:
        print("Please enter the amount in multiples of 100.")
else:
    print("Invalid PIN")


# output:
# Enter your PIN: 0000
# Enter the amount to withdraw: 25000
# Withdrawal successful! Please collect your cash.
# Current balance: 25000.