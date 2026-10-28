#  Give a 20% discount only to products costing more than ₹2,000. 

prices = [500, 1200, 2500, 3000, 1500, 5000] 
discounted_products = [price * 0.8 for price in prices if price > 2000]
print(f"Discounted products: {discounted_products}")

# output: Discounted products: [2000.0, 2400.0, 4000.0]