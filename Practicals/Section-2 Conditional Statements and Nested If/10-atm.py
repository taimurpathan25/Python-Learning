correct_pin = int(input("Enter your Pin : "))

if correct_pin != 1234:
    print("Incorrect PIN !, Again Enter Correct PIN")

else:
    active_account = input("Your Account is Active? (yes/no) : ");

    if active_account != "yes":
        print("Account is Not Active")

    else:
        amount_withdrawal = int(input("Enter Amount for Withdrawal : "))
        balance = 50000

        if amount_withdrawal <= 0:
            print("Amount must be Positive !")

        elif amount_withdrawal % 100 != 0:
            print("Amount must be a multiple of Rs 100")

        elif amount_withdrawal > balance:
            print("Insufficient Balance")

        elif balance - amount_withdrawal < 500:
            print("Minimum Balance Rs 500 is Required")

        elif amount_withdrawal > 20000:
            print("Extra Verification Required !")
            otp = int(input("Enter OTP for Verification : "))

            if otp != 4545:
             print("Incorrect OTP, Withdrawal Cancel")    
            else: 
                balance -= amount_withdrawal
                print("Withdrawal Successful !")
                print("Remaining Balance : ", balance)

        else:
            balance -= amount_withdrawal
            print("Withdrawal Successful !")
            print("Remaining Balance : ", balance)
            
            
            
# output:
# Enter your Pin : 1234
# Your Account is Active? (yes/no) : yes
# Enter Amount for Withdrawal : 30000
# Extra Verification Required !
# Enter OTP for Verification : 4545
# Withdrawal Successful !
# Remaining Balance :  20000