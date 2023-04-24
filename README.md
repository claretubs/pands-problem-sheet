# Problem Sheets 2023

## Table of Contents
* [Weekly Tasks](#weekly-tasks)
    * [Week 01 - Hello World](#week-01---hello-world)
    * [Week 02 - Bank](#week-02---bank)
    * [Week 03 - Accounts](#week-03---accounts)
    * [Week 04 - Collatz](#week-04---collatz)
    * [Week 05 - Weekday](#week-05---Weekday)
    * [Week 06 - Squareroot](#week-06---squareroot)
    * [Week 07 - Es](#week-07---es)
    * [Week 08 - Plot Task](#week-08---plot-task)
* [Technologies](#technolgies)

## **Weekly Tasks**

### ***Week 01 - Hello World***

This task was to allow me familiarise myself with cmder and VScode. I created a program called helloworld.py. It was a basic code used to print Hello World using python. I used the lecture slides and videos to help me create this code.

- - - -

### ***Week 02 - Bank***

>Write a program that can do the following:
>1. Prompt the user and read in two money amounts in cents.
>2. Add the two amounts.
>3. Print out the answer in a readable format in euro and have a decimal point between the euro and cent of the amount.

User must input two values in cents. To ensure the values are not interpreted as strings, the string input must be converted into an integer. The two inputs are then added together to find the total amount in cents. The important thing here is not forget to convert the final cents amount into euro, in order to get the desired result. The aim of this task was to find the final amount in euro without using floats (even hidden floats, e.g. /100). [Integer Division](https://stackoverflow.com/questions/183853/what-is-the-difference-between-and-when-used-for-division), otherwise known as floor division, divides the first arguement by the second and rounds the reuslt down to the nearest whole number. This method is used to find the value in euro. Then to find the remainder in cents, the [Modulus Operator](https://realpython.com/courses/python-modulo-operator/) is used. The modulus operator returns the remainder of dividing two numbers. Finally, the answer is printed out in a readable format. The remainder is rounded to two digits with the [:02d](https://splunktool.com/what-does-02d-mean-in-python). It formats an integer (d) to a field of miniumum width 2 (2), with zer-padding on the left (leading 0). It ensures the cents are always printed in two digits, even if they are zero.

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
python .\bank.py
```
User input :
```
Please enter your first amount in cents: 65
Please enter your second amount in cents: 180
```
Output :

```
The total amount of money is €2.45
```
</p>
</details>

- - - -

### ***Week 03 - Accounts***

>Write a python program called that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs). Modify the program to deal with account numbers of any length.

The function *replaced_account_number* takes in one arguement called *account_number* which is a string the user inputs. This is the account number that is going to be masked in the program. This function allows for an account number of any length, not just 10 characters. It checks the length of the account number and returns it unmodifed if it has a length of 4 or less. In the case stated previously, there are no chacaters to replace if there are 4 or less.

If the length of the account number is greater than 4 then a string called *replace* is created. The variable *replace* takes the [Length](https://www.geeksforgeeks.org/python-string-length-len/) of the account number and replaces all characters but the last 4 in the account number. The last 4 digits of the accoint number are appended to the end of the *replace* string, so that we have the last 4 digits of the account number and the first 6 digits replaced with 'X' characters. This is done using [Slicing](https://www.w3schools.com/python/python_strings_slicing.asp) The *new_account_number* calls the funtion.


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

- - - -

### ***Week 04 - Collatz***
> Write a python program that asks the user to input any positive integer and outputs the successive values of the following calculation:
>At each step calculate the next value by taking the current value and, if it is even, divide by two, but if it is odd, multiply it by three and add one.

User inputs any postive integer which is stored in the variable *number*. The *while* runs as long as *number* is not eqaul to 1. The print statment allows the current value of *number* to be printed at each iteration. In order to make the output list look neater, [end = ' '](https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/) parameter is used to seperate the numbers with a space instead of a newline character.

It is then determined whether that positive integer is even or odd, with the help of conditional statements *if* and *else*. The *if* statement checks if the positive inetger is even by using modulus operation. If the remainder of the operation is zero, the number is even. Hence, the program preforms the calculations (divide by 2) stated in the *if* statement and prints it out. [Integer Division](https://www.geeksforgeeks.org/division-operators-in-python/) *//* is used instead of regular dvision */*. Integer dvision returns the floor value (rounds down to the nearest whole number) for both integer and floating-point arguments. It is important to use this type of division as the desired result is an integer, which is required for the next iteration of the algorithm to work correctly. 

 However, if the remainder of the modulus operation is not zero, the program preforms the calculations (multiply by three and add one) stated in the *else* statment. This set of operations can otherwise be known as [Collatz Sequence Python](https://www.youtube.com/watch?v=lAp_5qTdOhM). Once *number* becomes 1, the loop terminates and the fianl value of *number* is printed to the screen.
 

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
 10 5 16 8 4 2 1
```
</p>
</details>

- - - -

### ***Week 05 - Weekday***
> Write program that outputs whether or not today is a weekday.

In order to manipulate the date and time in this program, a datetime module must be imported. This program does not require any user input. The program first determines the [Current Date](https://www.w3schools.com/python/python_datetime.asp) and then from that it determines what day of the week it is. The [Days of the Week](https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python) are stored as numbers, 0 to 6, 0 being Monday and 6 being Sunday.

A simple *if* statement can determine if it is a weekday or weekend. Saturday and Sunday are represented by the numbers 5 and 6. Therefore,any number below 5 is a weekday. 

To ensure this program is running correctly, it should be tested on a weekday and weekend.

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
python .\weekday.py
```
Output if Weekday :
```
Yes, unfortunately today is a weekday
```
Output if not Weekday:

```
It is the weekend, yay!
```
</p>
</details>

- - - -

### ***Week 06 - Squareroot***
>Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

This program required many hours of research. In order to make the program, it was vital to learn how [Newtons Method](https://calcworkshop.com/derivatives/newtons-method/) worked. Once this method was understood, it was just a matter of implementing mathemathical formulas. 

To ensure the input is a postive number, a *while* loop is incorporated into the program. If the number entered was zero or less, an error pops up informing the user they need to try again with a postive value. It is important to remember that the input value must be a float value.

The funtion was created using the key word *sqrt()*. To start this function, an intial guess (which is reasonably close to the true root) is assigned to the variable *x*. The intial guess is equal to the value entered by the user for the first iteration. [Newtons Method](https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/) is an iterative process, therefore, a *while* loop is necessary in the function. In order to count the iterations in the *while* loop, the *count* is initially set to zero. The *while* loop checks for one codition of convergance while the *if* statement checks for one other condition of convergance. The value *1e-9* was used in order to get as close as possible to zero. After the *if* statement the root is updated in the variable *x* and the iteration begins again. This process continues until the conditions are no longer true, and the function returns the value of the root. The value is rounded to one decimal place.

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
python .\squareroot.py
```
User input :
```
Please enter a postive number: 14.5
```
User input for negative value:
```
Please enter a postive number: -5
This is not a positive number
Try again! Any postive number: 14.5
```
Output :

```
 The sqaure root of 14.5 is approx 3.8
```
</p>
</details>

- - - -

### ***Week 07 - Es***
>Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line.

Program reads a text file called by the user from an arguement on the command line. In order to call upon the text file, it must be in the same directory as the program.

By importing [sys](https://docs.python.org/3.8/library/sys.html), the module provides acess to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. [sys.argv()](https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/) is an array for command line arguments in python. The script name is held in *argv[0]*. Therefore, the text filename is held in the second arguement, *argv[1]*.

The [With Open in Python](https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/) allows you to work with files by opening them. The *open()* function must be used in conjunction with the *close()* function. However, the *with* statement closes the file for you without being told to. There are two parameters in the *open()* function - the filename and the mode. The content of the file is stored in the variable *e*. Using the [Count](https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/) method all the e's in the text file (upper case and lower case) are found and added together.

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
python .\es.py file.txt
```
Output :

```
The letter 'e' shows up 9 times
```
</p>
</details>

- - - -

### ***Week 08 - Plot Task***
>Write a program called plottask.py that displays:
>
>* a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
>* and a plot of the function  h(x)=x^3 in the range [0, 10], 
>
>on the one set of axes.

This program required two modules to be imported in order to make the plots. These modules were *numpy* and *matplotlib.pyplot*. To ensure the random numbers generated for this task were the same each time it ran, the *seed()* method was used. A [Histogram](https://www.w3schools.com/python/matplotlib_histograms.asp) is made from the numbers the program randomly generates. As it follows, the values in the brackets are the mean, standard deviation and number of values. Once the histogram is made, the function *h(x) = x ^ 3* is plotted on the same graph. The function ranges from 1 to 10. 

The functions *title()*, *xlabel()* and *ylabel()* were taken from the *matplotlip.pyplot* library to label the plot. The fonts for all the [Labels](https://www.w3schools.com/python/matplotlib_labels.asp) were edited using the variables *font1* and *font2*. They set the style, size and colour of the font. A legend was made to help the user identify the histogram and function.

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
python .\plottask.py
```
Output :

```
An image of a plot will pop up once the program is run.
```
</p>
</details>

- - - -

## Technolgies 
  * Visual Studio Code - version 1.74.3
  * Cmder - version 1.3.20.151