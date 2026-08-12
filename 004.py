'''
Write a Python program that takes a temperature in Celsius from the user and converts it into Fahrenheit.

Formula:
Fahrenheit = (Celsius × 9/5) + 32

Conditions:

Use input()
Use a variable
Convert the input into a number
Don't use any module
Don't use a built-in conversion function

Example:

Enter temperature in Celsius: 25

Temperature in Fahrenheit: 77.0
'''





cels = int(input("Enter temperature in Celsius: "))

fahren = (cels*9/5) + 32

print("Temperature in Fahrenheit: ", fahren)