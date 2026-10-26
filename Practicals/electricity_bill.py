units = int(input("Enter the units consumed: "));
if units < 0:
    print("Invalid Input");
else:
    if units <= 100:
       bill = units * 5;
       print("Your 5 Rs Per unit bill is:", bill);
    elif units <= 200:
         bill = units * 7;
         print("Your 7 Rs Per unit bill is:", bill);
    elif units <= 300:
         bill = units * 10;
         print("Your 10 Rs Per unit bill is:", bill);
    else:
         bill = units * 15;
         print("Your 15 Rs Per unit bill is:", bill);

    if bill > 3000:
        bill += bill * 10/100;
        print("After Included 10% Surcharge \nnow! your bill is : ", bill);