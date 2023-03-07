# Problem Sheets 2023

## Table of Contents
* [Weekly Tasks](#weekly-tasks)
    * [Week 01 - Hello World](#week-01---hello-world)
    * [Week 02 - Bank](#week-02---bank)
    * [Week 03 - Accounts](#week-03---accounts)
    * [Week 04 - Collatz](#week-04---collatz)
* [Resources](#rescources)
* [Technologies](#technolgies)

## **Weekly Tasks**

### ***Week 01 - Hello World***

This task was to allow me familiarise myself with cmder and VScode. I created a program called helloworld.py. It was a basic code used to print Hello World using python. I used the lecture slides and videos to help me create this code.  

### ***Week 02 - Bank***

>Write a program that can do the following:
>1. Prompt the user and read in two money amounts in cents.
>2. Add the two amounts.
>3. Print out the answer in a readable format in euro and have a decimal point between the euro and cent of the amount.

User must input two values in cents. To ensure the values are not interpreted as strings, the string input must be converted into an integer. The two inputs are then added together. The important thing here is not forget to convert the final cents amount into euro, in order to get the desired result. A float value will allow the decimal point to be in the answer.

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
python .\bank.py
```
User input :
```
Please enter your first amount in cents: 58
Please enter your second amount in cents: 70
```
Output :

```
The total amount of money is €1.28
```
</p>
</details>

### ***Week 03 - Accounts***

>Write a python program called that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

User inputs a string of 10 characters long as their account number. and out the account number with only the last 4 digits showing and having the first 6 digits replaced with X's.

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
python .\accounts.py
```
User input :
```
Please enter your 10 digit account number: 1234567890
```
Output :

```
Your account number is: XXXXXX7890
```
</p>
</details>

### ***Week 04 - Collatz***
> Write a python program that asks the user to input any positive integer and outputs the successive values of the following calculation:
>At each step calculate the next value by taking the current value and, if it is even, divide by two, but if it is odd, multiply it by three and add one.

User inputs any postive integer. It is then determined whether that positive integer is even or odd, with the help of conditional statements *if* and *else*. The *if* statement checks if the positive inetger is even by using modulus operation. If the remainder of the operation is zero, the number is even. Hence, the program preforms the calculations (divide by 2) stated in the *if* statement and prints it out. However, if the remainder of the modulus operation is not zero, the program preforms the calculations (multiply by three and add one) stated in the *else* statment. This set of operations can otherwise be known as [Collatz Sequence Python](https://www.youtube.com/watch?v=lAp_5qTdOhM)

The *while* loop ensures the step outlined above is repeated for every number until it reaches one. It also allows for list of numbers to be created. In order to make the output list look neater, two steps were carried out. Originally, each value of the output was displayed on a new line. [Print without a New Line](https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/) made the results more compact and easier to read. [Square Bracket Removal](https://python.engineering/python-remove-square-brackets-from-list/) was to remove the sqaure brackets at either side of the list to acieve the desired result. 

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
python .\collatz.py
```
User input :
```
Please Enter a Positive integer: 10
```
Output :

```
10, 5, 16, 8, 4, 2 
```
</p>
</details>

## Rescources

## Technolgies 
  * Visual Studio Code - version 1.74.3
  * Cmder - version 1.3.14.982

