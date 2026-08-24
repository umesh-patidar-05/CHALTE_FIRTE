'''
Python String Assessment
String Analyzer

Write a Python program that accepts a string from the user and performs the following operations:

1. Find and display the length of the string.
2. Display the string in uppercase and lowercase.
3. Count and display the number of occurrences of a character entered by the user.
4. Check whether the string starts with a vowel (a, e, i, o, u), ignoring case.
5. Reverse the given string using string slicing.
6. Check whether the given string is a palindrome or not.
7. Remove all spaces from the string and display the resulting string.
8. Display the first character and last character of the string.

Example Input
Enter a string: Python is easy
Enter a character to count: y

Expected Output
Length: 14
Uppercase: PYTHON IS EASY
Lowercase: python is easy
Count of 'y': 2
Starts with vowel: False
Reverse: ysae si nohtyP
Palindrome: False
String without spaces: Pythoniseasy
First character: P
Last character: y


Conditions
Use built-in string methods wherever appropriate.
For reversing the string, use slicing.
The vowel check should work for both uppercase and lowercase input.
Do not use any external library.
'''






string = input("Enter a string: ")
character = input("Enter a character to count: ")

print("Length:", len(string))

print("Uppercase:", string.upper())
print("Lowercase:", string.lower()) 

count = string.lower().count(character.lower())
print("Count of", character, ":", count)

vow = False
if string[0].lower() in "aeiou":
    vow = True

print("Starts with vowel:", vow)

print("Reverse: ", string[::-1])

if string == string[::-1]:
    print("Palindrome: TRUE")
else:    
    print("Palindrome: FALSE")

without = ""
for i in string:
    if i !=" ":
        without += i 
print("String without spaces:", without)

print("First character:", string[0])
print("Last character:", string[-1])
