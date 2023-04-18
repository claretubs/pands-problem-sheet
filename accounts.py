# Program that reads 10 character account numbers
# It only outputs the last 4 digits and the first 6 are replaced by x's
# Author: Clare Tubridy
# Date: 09/02/2023

# Function created to replace all digits apart from the last 4 with x's
def replaced_account_number(account_number):
    # If the length of the account number is 4 or smaller, return the account number unaltered.
    if len(account_number) <=4:
        return account_number
    
    # Replaces all digits in the account with a X, except the last 4 digits.
    replace = 'X' * (len(account_number) - 4)
    replace += account_number[-4:]

    return replace

# User input
account_number = input("Please enter your 10 digit account number: ")
# Variable calls the function
new_account_number = replaced_account_number(account_number)

print(f"Your account number is: {new_account_number}")