#  Give a 10% discount to products costing ₹1,000 or more; otherwise, give a 5% discount. Store the final prices in a new list.  

prices = [500, 1200, 800, 2000, 1500]
final_prices = [price * 0.90 if price >= 1000 else price * 0.95 for price in prices]
print(final_prices)

# output:
# [475.0, 1080.0, 760.0, 1800.0, 1350.0]