# Program takes a positive floating-point number
# and outputs an approximation of its sqaure root
# Author: Clare Tubridy
# 09-03-2023

# To ensure the input is a positive integer
number = float(input("Please enter a postive number: "))
while number < 1:
    print("This is not a positive number")
    number = float(input("Try again! Any postive number: "))


# Function to return the sqaureroot of a number using Newtons Method
def sqrt(number):

    x = number                              # set inital guess for sqaure root
    count = 0                               # count numbers of iterations

    while True:
        count += 1

        root = 0.5 * (x + (number / x))    

        if abs(root - x) < 1e-9:
            break
        x = root                            # update root

    return root

n = round(sqrt(number),1)                   # round to one decimal place

print(f"The sqaure root of {number} is approx {n}")