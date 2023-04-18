# bank.py
# Author: Clare Tubridy
# Date: 07/02/2023
# Reads two amounts in cents, adds them together and outputs the euro decimal amount.

# Prompts user to enter amount 1 in cents
money1=int(input("Please enter your first amount in cents: "))
# Prompts user to enter amount 2 in cents
money2=int(input("Please enter your second amount in cents: "))

# Adds the two amounts together.
total_amount = money1 + money2

# Integer division('//') instead of regular division('/')
# Finds total amount in euro
euros = total_amount // 100
# Modulus used to find remainder. In this case the remainder is equal to cents
cents = total_amount % 100

# Cents is gotten to 2 decimal places by "":02d"
print(f"The total amount of money is €{euros}.{cents:02d}")