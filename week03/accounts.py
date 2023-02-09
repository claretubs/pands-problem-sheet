#Program that reads 10 character account numbers
#It only outputs the last 4 digits and the first 6 are replaced by x's
#Author: Clare Tubridy
#Date: 09/02/2023

account_number = input("Please enter your 10 digit account number: ")

print(f"Your account number is: XXXXXX{account_number[6:]}")