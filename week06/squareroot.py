# Program takes a positive floating-point number
# and outputs an approximation of its sqaure root
# Author: Clare Tubridy
# 09-03-2023

# Function to ensure the input is a positive integer
def readNum():
    number = float(input("Please enter a postive number: "))
    while number <= 1:
        print("This is not a positive number")
        number = float(input("Try again! Any postive number: "))

num = readNum()

# Function to return the sqaureroot of a number
# Using Newtons Method
def sqrt(n):

    x = n
    count = 0

    while (1):
        count += 1

        root = 0.5*(x + (n / x))

        if (abs(root - x) < 1):
            break
        x = root
    return root

sqaureroot = sqrt(readNum())
print(f"The sqaure root of {num} is approx {sqaureroot}")

