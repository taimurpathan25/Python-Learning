# write a program for ATM withdrawal
correct_pin = 1234
balance = 50000

pin = int(input("enter the pin : "));
if pin != correct_pin:
    print("Invalid PIN, please enter correct PIN");
else:
    amount = int(input("Enter the Amount : "));
    if amount % 100 != 0:
       print("please enter correct money");
    elif amount >= balance:
       print("InSufficient Balance !");
    else:
        balance -= amount
        print("Withdrawal Successfull !");
        print("Your Remaining Balance is :", balance);