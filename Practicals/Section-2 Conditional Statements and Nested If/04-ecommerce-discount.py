# E-Commerce Discount 
# An online shopping website provides discounts based on the following conditions: 
# - If cart amount >= ₹5,000: 
# - If the customer is a premium member, discount = 20%. 
# - Otherwise, discount = 10%. 
# - If cart amount < ₹5,000: 
# - If the customer is a premium member, discount = 5%. 
# - Otherwise, no discount. 
# - Print the final amount. 

cart_amount = float(input("Enter the cart amount: "))
is_premium_member = input("Are you a premium member? (yes/no): ").strip().lower()
if cart_amount >= 5000:
    if is_premium_member == "yes":
        discount = cart_amount * 0.20
        print(f"Congratulations! You are eligible for a 20% discount. Your discount amount is: ₹{discount:.2f}")
    else:
        discount = cart_amount * 0.10
        print(f"You are eligible for a 10% discount. Your discount amount is: ₹{discount:.2f}")
else:
    if is_premium_member == "yes":
        discount = cart_amount * 0.05
        print(f"Congratulations! You are eligible for a 5% discount. Your discount amount is: ₹{discount:.2f}")
    else:
        discount = 0.0
        print("You are not eligible for any discount.")
final_amount = cart_amount - discount
print(f"Final amount after discount: ₹{final_amount:.2f}")



# output:
# Enter the cart amount: 25000
# Are you a premium member? (yes/no): yes
# Congratulations! You are eligible for a 20% discount. Your discount amount is: ₹5000.00
# Final amount after discount: ₹20000.00