'''
Question — Variables + Input + Operators
Write a Python program that:
Takes the user's name
Takes their age
Takes their current city
Calculates what their age will be after 5 years
Prints the information in a meaningful format.

Example input:
Enter your name: Umesh
Enter your age: 21
Enter your city: Indore

Expected output:
Hello Umesh!
You are currently 21 years old.
You live in Indore.
After 5 years, you will be 26 years old.

Condition: Use variables and input(). Don't hard-code the result.
'''





name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print(f"Hello {name}!")
print(f"You are currently {age} years old.")
print(f"You live in {city}.")
print(f"After 5 years, you will be {age + 5} years old.")