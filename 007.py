'''
Question — String Analyzer

User से एक string input लो और:

String की length निकालो।
String को uppercase में print करो।
String को lowercase में print करो।
उसमें कितने vowels (a, e, i, o, u) हैं, count करो।
String को reverse करके print करो।
Check करो कि string palindrome है या नहीं।

Example:

Enter string: madam


Length: 5
Uppercase: MADAM
Lowercase: madam

Vowels: 2
Reverse: madam
Palindrome: True
'''





s = input("Enter a string: ")
vowel_count = 0
for i in s:
    if i.lower() in "aeiou":
        vowel_count += 1

print("Length:",len(s))        
print("Uppercase:",s.upper())
print("Lowercase:", s.lower())
print("Vowels:", vowel_count)
print("Reverse:", s[::-1])
print("Palindrome:", s == s[::-1])
