# Shopping Cart Classification A dictionary contains products and their prices. Classify each product
# Conditions: 
# - Price >= ₹5,000 -> Premium Product 
# - Price >= ₹1,000 but < ₹5,000 -> Expensive Product 
# - Price < ₹1,000 -> Affordable Product

products = { 
    "Mobile": 15000,
    "Mouse": 500,         
    "Laptop": 60000,         
    "Keyboard": 1200     
}

for product, price in products.items():
    if price >= 5000:
        category = "Premium Product"
    elif price >= 1000:
        category = "Expensive Product"
    else:
        category = "Affordable Product"

    print(f"{product}: {price} - {category}")
    
    
# output:
# Mobile: 15000 - Premium Product
# Mouse: 500 - Affordable Product
# Laptop: 60000 - Premium Product
# Keyboard: 1200 - Expensive Product
