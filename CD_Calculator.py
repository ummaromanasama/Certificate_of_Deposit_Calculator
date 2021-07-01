# Input the deposit amount
year = int(input('Enter the intial year of the CD account: '))

# Input the deposit amount
amount = int(input('Enter the deposit amount: '))

# Input the annual interest rate.
annual_interest_rate = float(input('Enter the annual interest rate (%): '))
annual_interest_rate /= 100

# Input number of years account will earn interest.
time = int(input('Enter how many years the account will accrue interest: '))

year += time

# The compund rate is monthly.
compound = 12

# Calculate the total amount
total_amount = (amount * (1 + annual_interest_rate/ compound) ** (compound * time))
total_intrest = total_amount - amount

# Display the total amount.
print('At the end of', year,'you will have $',format(total_amount, '.2f'))
print('The total amount of interest accumulated is $',format(total_intrest, '.2f'))