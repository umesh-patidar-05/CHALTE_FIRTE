'''
Write a Python program to take the number of rows and columns as input from the user,"
"create a 2D list (matrix) by taking elements from the user, "
"and display it in matrix format.
'''





rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    l =[]
    for j in range(columns):
        l.append(input(f"Enter [{i}][{j}]: "))

    matrix.append(l)

# print(matrix)
print("Matrix is: ")
for i in matrix:
    for j in i:
        print(j, end=" ")
    print()



