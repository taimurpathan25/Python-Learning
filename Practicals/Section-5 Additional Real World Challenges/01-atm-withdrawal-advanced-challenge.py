# ATM Withdrawal Advanced Challenge
# Conditions: 
# - PIN must be correct. 
# - Account must be active. 
# - Withdrawal amount must be positive. 
# - Withdrawal amount must be a multiple of ₹100. 
# - Balance must be sufficient. 
# - After withdrawal, a minimum balance of ₹500 must remain. 
# - Amount > ₹20,000 -> Extra verification. 

pin = 1234;
account_active = True;
balance = 25000;

entered_pin = int(input("Enter Your PIN : "));
if entered_pin != pin:
    print("Invalid Pin!")
elif not account_active:
    print("Account is not Active!")
else: 
    amount = int(input("Enter withdrawal Amount (₹): "))
    if amount <= 0:
        print("Withdrawal Amount Must be Positive")
    elif amount % 100 != 0:
        print("Amount must be a Multiple of 100")
    elif amount > balance:
        print("InSufficient Balance !")
    elif balance - amount < 500:
        print("Must Remaining Balance Minimum ₹500")
    elif amount > 20000:
        print("Extra Verification Required !")
        verification = input("Enter verification code (Yes/NO)")
        if verification == "YES".lower():
            balance = balance - amount
            print("Withdrawal Successfull !")
            print("Remaining balance is ₹",balance)
        else: 
            print("Verification Failed, Transaction Cancelled !")
    else:
        balance -= amount
        print("Withdrawal successful!")
        print("Remaining balance: ₹", balance)
        
        
# output :
# Enter Your PIN : 1234
# Enter withdrawal Amount (₹): 35000
# InSufficient Balance !

# Enter Your PIN : 1234
# Enter withdrawal Amount (₹): 15000
# Withdrawal successful!
# Remaining balance: ₹ 10000

# Enter Your PIN : 1234
# Enter withdrawal Amount (₹): 1
# Amount must be a Multiple of 100

# Enter Your PIN : 1245
# Invalid Pin!
    