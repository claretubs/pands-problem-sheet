#Program that reads 10 character account numbers
#It only outputs the last 4 digits and the first 6 are replaced by x's
#Author: Clare Tubridy
#Date: 09/02/2023

account_number = input("Please enter your 10 digit account number: ")

x = 'XXXXXX'

# The two variables are merged together

print(f"Your account number is:{x + account_number[6:]}")