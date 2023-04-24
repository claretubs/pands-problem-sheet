# Program that reads any postive integer from user
# Outputs the successive values of the following calculation:
# At each step calculate the next value by taking the current value and,
# If it is even, divide it by two,
# But if it is odd, multiply it by three and add one
# If the current value is 1, have program end.
# Author: Clare Tubridy
# Date: 01/03/2023

number = int(input("Please Enter a Positive integer: "))

while number != 1:                          # continues loop until value reaches 1

    # current value of num is printed at each iteration
    print(number, end = ' ')                # end parameter seperates the numbers with a space instead of a newline character
    
    if (number % 2) == 0:                   # even numbers
        number = number // 2                # even number gets divided by 2 using integer division('//') instead of regular division('/')
    else:                                   # odd numbers
        number = (number * 3) + 1           # odd number gets multiplied by 3 and then 1 is added.

print(number)          