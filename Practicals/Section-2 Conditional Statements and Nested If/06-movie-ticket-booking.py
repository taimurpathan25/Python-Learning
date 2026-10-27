# Create Movie Ticket Booking System
# conditions:
# - Check whether seats are available. 
# - If seats are available, check customer age: 
# - Age < 5 -> Free 
# - Age 5-12 -> 50% discount 
# - Age > 60 -> 30% discount 
# - Otherwise -> Full price 
# - If no seats are available, print "House Full".

# Define the total number of seats available
total_seats = 10
ticket_price = 100.0  # Full price of the ticket
requested_seats = int(input("Enter the number of seats you want to book: "))
if requested_seats <= total_seats:
    age = int(input("Enter your age: "))
    if age < 5:
        final_price = 0.0
        print("You are eligible for a free ticket. Your final price is: Rs", final_price)
    elif 5 <= age <= 12:
        final_price = ticket_price * 0.5 * requested_seats
        print("You are eligible for a 50% discount. Your final price is: Rs", final_price)
    elif age > 60:
        final_price = ticket_price * 0.7 * requested_seats
        print("You are eligible for a 30% discount. Your final price is: Rs", final_price)
    else:
        final_price = ticket_price * requested_seats
        print("You are not eligible for any discount. Your final price is: Rs", final_price)
else:
    print("House Full")