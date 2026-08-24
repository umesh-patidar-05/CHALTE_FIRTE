'''
Student Marks Analyzer

Write a Python program that accepts 5 marks from the user and stores them in a list. Perform the following operations:

1. Display the complete list of marks.
2. Display the total number of marks stored in the list.
3. Find and display the highest mark.
4. Find and display the lowest mark.
5. Calculate and display the sum of all marks.
6. Calculate and display the average of the marks.
7. Sort the list in ascending order.
8. Sort the list in descending order.
9. Ask the user for a mark and check whether that mark exists in the list.
10. Ask the user for a mark and find how many times it occurs in the list.
11. Add a new mark to the list.
12. Remove a mark entered by the user from the list.
13. Display the final updated list.

Example Input
Enter 5 marks:
Enter mark 1: 78
Enter mark 2: 65
Enter mark 3: 92
Enter mark 4: 65
Enter mark 5: 84

Enter mark to search: 65
Enter mark to remove: 78

Expected Output
Original List: [78, 65, 92, 65, 84]
Number of marks: 5
Highest Mark: 92
Lowest Mark: 65
Sum: 384
Average: 76.8

Ascending Order: [65, 65, 78, 84, 92]
Descending Order: [92, 84, 78, 65, 65]

65 exists in the list.
65 occurs 2 times.

List after adding new mark: [...]
List after removing 78: [...]
Final List: [...]
Conditions
Use a list to store all marks.
Use appropriate list methods wherever possible.
Do not create separate variables for each mark.
The program should work even when the same mark occurs multiple times.
Handle the removal operation appropriately if the entered mark is not present.
'''






marks = []
print("Enter 5 marks: ")
for i in range(5):
    e = int(input(f"Enter mark {i+1}: "))
    marks.append(e)

# print(marks)    

search = int(input("Enter marks to search: "))
remove = int(input("Enter marks to remove: "))

print("Original list:", marks)
print("Number of marks: ", len(marks))

marks.sort()

print("Highest mark: ", marks[-1])
print("Lowest mark: ", marks[0])

print("Sum:", sum(marks))

print("Average:", sum(marks)/ len(marks))

print("Ascending Order:", marks)
desc = marks[::-1]
print("Descending Order:", desc)

if search in marks:
    print(f"{search} exists in the list")
else:    
    print(f"{search} exists not in the list")

occur = marks.count(search)
print(f"{search} occurs {occur} times.")

new = int(input("Enter new mark: "))
marks.append(new)

print("List after adding new mark:", marks)

marks.remove(remove)
print(f"List after removing {remove}: ", marks)

print("Final list: ", marks)