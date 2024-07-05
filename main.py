import math

print("Choose either 'investment' or 'bond' from the menu below or proceed: \n Investment     "
      "-To calculate the amount of interest you'll earn on interest \n  bond    "
      "      -To calculate the amount you will have to pay on home loan on interest\n")


choice = input("Enter 'investment' or 'bond': ").lower()

if choice == 'investment':
    amount = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate: ")) / 100
    years = float(input("Enter the number of years you plan to invest for: "))
    interest_type = input("Do you want 'simple' or 'compound' interest? ").lower()

    if interest_type == 'simple':
        total_amount = amount * (1 + interest_rate * years)
        print(f"The total amount after {years} years with simple interest is: {total_amount:.2f}")
    elif interest_type == 'compound':
        total_amount = amount * math.pow((1 + interest_rate), years)
        print(f"The total amount after {years} years with compound interest is: {total_amount:.2f}")
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")

elif choice == 'bond':
    present_value = float(input("Enter the present value of the house: "))
    annual_interest_rate = float(input("Enter the annual interest rate: ")) / 100
    months = float(input("Enter the number of months you plan to take to repay the bond: "))

    monthly_interest_rate = annual_interest_rate / 12
    repayment = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -months))
    print(f"The monthly repayment amount is: {repayment:.2f}")

else:
    print("Invalid choice. Please enter 'investment' or 'bond'.")

