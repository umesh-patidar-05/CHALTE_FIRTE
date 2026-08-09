'''
Question 1 — Lists + Loops

Write a Python program that takes a list of numbers:

numbers = [12, 5, 8, 21, 10, 3, 18]

and finds:

The largest number
The smallest number
The sum of all numbers
The average

Condition: Don't use max(), min(), sum(), or statistics.
'''




n = int(input("Enter number of elements in list: "))
listt = []

for i in range(n):
    listt.append(int(input(f"Enter {i}st element: ")))

print("List is: ",listt) 

largest = listt[0]
smallest = listt[0]
summ = 0

for i in listt:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

    summ += i

print("REUSLT: ")

print("Largest number is: ", largest)
print("Smallest number is:", smallest)
print("Sum is: ", summ)
print("Average is : ", summ/n)