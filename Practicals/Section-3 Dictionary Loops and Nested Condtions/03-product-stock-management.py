# Product Stock Management A dictionary contains products and their available stock. Use a loop and nested conditions to display the stock status. 
# Conditions: 
# - Stock == 0 -> Out of Stock 
# - Stock <= 5 -> Low Stock 
# - Stock > 5 -> Available 


  
products = {
    "Laptop": 10,
    "Mouse": 3,
    "Keyboard": 0,
    "Monitor": 7,
    "Printer": 2
}

for product, stock in products.items():
    if stock == 0:
        status = "Out of Stock"
    elif stock <= 5:
        status = "Low Stock"
    else:
        status = "Available"
    print(f"{product}: {stock} - {status}")
    

# output:
# Laptop: 10 - Available
# Mouse: 3 - Low Stock
# Keyboard: 0 - Out of Stock
# Monitor: 7 - Available
# Printer: 2 - Low Stock