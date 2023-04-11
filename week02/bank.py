# bank.py
# Author: Clare Tubridy
# Date: 07/02/2023
# Reads two amounts in cents, adds them together and outputs the euro decimal amount.

money1=int(input("Please enter your first amount in cents: "))     # inputs amount 1 in cents
money2=int(input("Please enter your second amount in cents: "))    # inputs amount 2 in cents

tmoney=(money1+money2)/100  # finds total amount of money in euro

print(f"The total amount of money is €{tmoney}")