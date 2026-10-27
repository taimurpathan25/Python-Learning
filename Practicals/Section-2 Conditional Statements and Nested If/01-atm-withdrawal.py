# write the  python program for ATM withdrawal.

correct_pin = "0000"
balance = 50000

pin = input("Enter your PIN: ")

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
