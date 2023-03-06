# Problem Sheets 2023

## Table of Contents
* [Weekly Tasks](#weekly-tasks)
    * [Week 01 - Hello World](#week-01---hello-world)
    * [Week 02 - Bank](#week-02---bank)
    * [Week 03 - Accounts](#week-03---accounts)
    * [Week 04](#week-04)
* [Resources](#rescources)
* [Technologies](#technolgies)

## Weekly Tasks

### **Week 01 - Hello World**

This task was to allow me familiarise myself with cmder and VScode. I created a program called helloworld.py. It was a basic code used to print Hello World using python. I used the lecture slides and videos to help me create this code.  

### **Week 02 - Bank**

>Write a program that can do the following:
>1. Prompt the user and read in two money amounts in cents.
>2. Add the two amounts.
>3. Print out the answer in a readable format in euro and have a decimal point between the euro and cent of the amount.

User must input two values in cents. To ensure the values are not interpreted as strings, the string input must be converted into an integer. The two inputs are then added together. The important thing here is not forget to convert the final cents amount into euro in order to get the desired result. A float value will allow the decimal point to be in the answer.

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
Please enter your first amount in cents: 70
```
Output :

```
The total amount of money is €1.28
```
</p>
</details>

### **Week 03 - Accounts**

>Write a python program called that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

The program in this task is called accounts.py and the purpose of it is to read a 10 character account number and out the account number with only the last 4 digits showing and having the first 6 digits replaced with X's.

### **Week 04**
> Write a python program that asks the user to input any positive integer and outputs the successive values of the following calculation:

>At each step calculate the next value by taking the current value and, if it is even, divide by two, but if it is odd, mulitiply it by three and add one.

[Square Bracket Removal](https://python.engineering/python-remove-square-brackets-from-list/)
[Collatz Sequence Python](https://www.youtube.com/watch?v=lAp_5qTdOhM)

## Rescources

## Technolgies 
  * Visual Studio Code - version 1.74.3
  * Cmder - version 1.3.14.982

