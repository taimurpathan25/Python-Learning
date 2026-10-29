#  Find products costing more than ₹1,000. 

prices = [499, 1299, 799, 2499, 999, 1599]
expensive_products = [price for price in prices if price > 1000]
print(expensive_products)


# output:
# expensive products : [1299, 2499, 1599]