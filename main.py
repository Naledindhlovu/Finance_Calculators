import math

def display_menu():
    print(" ")
    print("Choose either 'investment' or 'bond' from the menu below to proceed:")
    print(" ")
    print("1. Investment - to calculate the amount of interest you'll earn on interest")
    print("2. Bond - to calculate the amount you'll have to pay on a home loan")
    print("0. Exit")
    print(" ")
    selection = input("\nEnter your choice: ")
    
    if selection.isdigit():
        return int(selection)
    else:
        return -1  # Invalid input

def calculate_simple_interest(deposit, rate, years):
    amount = deposit * (1 + rate / 100 * years)
    print(" ")
    print(f"Your amount with simple interest is: {amount:.2f}")
    print(" ")

def calculate_compound_interest(deposit, rate, years):
    amount = deposit * math.pow((1 + rate / 100), years)
    print(" ")
    print(f"Your amount with compound interest is: {amount:.2f}")
    print(" ")

def calculate_bond_repayment(present_value, monthly_interest, months):
    monthly_interest /= 100
    repayment = (monthly_interest * present_value) / (1 - math.pow((1 + monthly_interest), -months))
    print(" ")
    print(f"Your monthly repayment is: R{repayment:.2f}")
    print(" ")

def handle_investment():
    deposit = float(input("Enter the amount of money you want to deposit: "))
    years = int(input("Enter the number of years you plan to invest: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    
    interest_type = input("Choose interest type - 's' for Simple, 'c' for Compound: ").lower()
    
    if interest_type == 's':
        calculate_simple_interest(deposit, rate, years)
    elif interest_type == 'c':
        calculate_compound_interest(deposit, rate, years)
    else:
        print("Invalid choice. Please enter 's' for Simple or 'c' for Compound.")

def handle_bond():
    present_value = float(input("Enter the present value of the house: "))
    monthly_interest = float(input("Enter the monthly interest rate (in %): "))
    months = int(input("Enter the number of months to repay the bond: "))
    
    calculate_bond_repayment(present_value, monthly_interest, months)

def main():
    while True:
        choice = display_menu()
        
        if choice == 1:
            handle_investment()
        elif choice == 2:
            handle_bond()
        elif choice == 0:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 for Investment, 2 for Bond, or 0 to Exit.")

if __name__ == "__main__":
    main()
