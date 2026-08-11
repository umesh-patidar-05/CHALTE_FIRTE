'''
Write a Python program that takes two numbers from the user and prints:

Their sum
Their difference
Their product
Their division
Their remainder

Conditions:

Use input()
Convert the input into numbers
Use variables and arithmetic operators
Don't use any module

Don't use built-in functions like sum()

Example:

Enter first number: 15
Enter second number: 4

Sum: 19
Difference: 11
Product: 60
Division: 3.75
Remainder: 3
'''





n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

summ = n1+n2
difference = n1 - n2
product = n1 * n2
division = n1/n2
reaminder = n1 % n2



print("Sum:",summ)
print("Difference:", difference)
print("Product:", product)
print("Division: ", division)
print("Remainder:", reaminder)