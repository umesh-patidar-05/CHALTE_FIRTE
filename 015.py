'''
🐍 Question: Exception Handling

Write a Python program that:

Takes two numbers from the user.
Performs division of the first number by the second.
Handles the situation when the user enters 0 as the second number.
Also handles the situation when the user enters non-numeric input.
Displays a suitable message for each error.
If there is no error, display the result.

Example:

Enter first number: 20
Enter second number: 5
Result: 4.0
'''


try: 
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    res = a/b
except ValueError as e:
    print('ValueError: ', e)

except ZeroDivisionError as e:
    print('ZeroDivisionError: ', e)

else:
    print(res)
    print('done')

finally:
    print("THANK-YOU")