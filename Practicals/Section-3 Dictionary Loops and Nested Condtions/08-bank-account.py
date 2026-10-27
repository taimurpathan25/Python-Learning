#  Bank Account Classification A dictionary contains customer names and account balances. 
# Conditions: 
# - Balance >= ₹10,000 -> Premium Account 
# - Balance > 0 but < ₹10,000 -> Regular Account 
# - Balance == 0 -> No Balance 
# - Balance < 0 -> Overdraft 

accounts = {
    "Rahul": 25000,
    "Amit": 5000, 
    "Priya": 0, 
    "Neha": -2000     
} 

for customer, balance in accounts.items():
    if balance >= 10000:
        account_type = "Premium Account"
    elif balance > 0:
        account_type = "Regular Account"
    elif balance == 0:
        account_type = "No Balance"
    else:
        account_type = "Overdraft"
    
    print(f"{customer}: Balance: ₹{balance} - {account_type}")
    
    
# Output:
# Rahul: Balance: ₹25000 - Premium Account
# Amit: Balance: ₹5000 - Regular Account
# Priya: Balance: ₹0 - No Balance
# Neha: Balance: ₹-2000 - Overdraft