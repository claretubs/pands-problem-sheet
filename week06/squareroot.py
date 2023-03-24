# Program takes a positive floating-point number
# and outputs an approximation of its sqaure root
# Author: Clare Tubridy
# 09-03-2023

# Function to ensure the input is a positive integer

def readNum():
    number = float(input("Please enter a postive number: "))
    while number < 1:
        print("This is not a positive number")
        number = float(input("Try again! Any postive number: "))

num = readNum()

# Function to return the sqaureroot of a number
# Using Newtons Method
def sqrt(num):

    x = num                        # set inital guess for sqaure root

    while True:

        root = 0.5 * (x + (num / x))

        if abs(root - x) < 1e-9:
            return root

        #x = root

print(f"The sqaure root of {num} is approx {sqrt(num)}")

