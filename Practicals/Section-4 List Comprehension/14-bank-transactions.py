# Bank Transactions Positive values represent deposits. Find all deposits and all withdrawals. 

transactions = [5000, -2000, 3000, -1000, 7000, -500] 
deposits = [transaction for transaction in transactions if transaction > 0]
withdrawals = [transaction for transaction in transactions if transaction < 0]
print(f"Deposits: {deposits}")
print(f"Withdrawals: {withdrawals}")
