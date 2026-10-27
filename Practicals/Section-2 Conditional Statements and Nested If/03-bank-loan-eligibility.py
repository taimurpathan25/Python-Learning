# Bank Loan Eligibility Program

age = int(input("Enter your age: "))
income = int(input("Enter your monthly income: "))

if age >= 21 and income >= 25000:

    credit_score = int(input("Enter your credit score: "))
    if credit_score >= 750:
        print("Loan Approved")
        interest_rate = 8.0

    elif credit_score >= 600:
        print("Loan Approved with High Interest Rate")
        interest_rate = 12.0

    else:
        print("Loan Rejected")
        interest_rate = 0

    if interest_rate > 0:

        loan_amount = float(input("Enter loan amount: "))
        loan_duration = int(input("Enter loan duration in years: "))

        # EMI calculation
        monthly_rate = interest_rate / (12 * 100)
        months = loan_duration * 12

        emi = (
            loan_amount
            * monthly_rate
            * (1 + monthly_rate) ** months
            / ((1 + monthly_rate) ** months - 1)
        )

        total_payment = emi * months
        total_interest = total_payment - loan_amount

        print("----- Loan Details -----")
        print("Interest Rate:", interest_rate, "% per year")
        print("Loan Amount:", loan_amount)
        print("Loan Duration:", loan_duration, "years")
        print("Monthly EMI:", round(emi, 2))
        print("Total Interest:", round(total_interest, 2))
        print("Total Payment:", round(total_payment, 2))
        print("Loan will be completed after", loan_duration, "years.")

else:
    print("Loan Rejected")