'''
QNO 1: Matrix Transpose & Diagonal Transformation(3.5 marks)

Write a Python program that accepts an N × N square matrix from the user.

The program must:

Display the original matrix.
Find and display the Main Diagonal elements.
Find and display the Secondary Diagonal elements.
Create the transpose of the matrix.
In the transposed matrix, swap each Main Diagonal element with the corresponding Secondary Diagonal element.
Display the final matrix.
The original matrix must not be modified.
Input
Enter the size of matrix: 4

Enter matrix elements:
10 20 30 40
50 60 70 80
90 15 25 35
45 55 65 75
Expected Output
Original Matrix:
10 20 30 40
50 60 70 80
90 15 25 35
45 55 65 75

Main Diagonal Elements:
10 60 25 75

Secondary Diagonal Elements:
40 70 15 45

Transpose Matrix:
10 50 90 45
20 60 15 55
30 70 25 65
40 80 35 75

Final Matrix After Diagonal Swapping:
45 50 90 10
20 15 60 55
30 25 70 65
75 80 35 40


Conditions
Use Python nested lists.
Matrix size must be taken from the user.
Do not use NumPy.
Do not use zip().
Do not use built-in matrix operations.
Do not modify the original matrix.

==========================
'''





n = int(input("Enter the size of matrix: "))

matrix = []

print("Enter matrix element: ")
for row in range(n):
    list = []
    for column in range(n):
        list.append(int(input()))
    matrix.append(list) 

print()
print("Original Matrix: ")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = " " )
    print()

main_diagonal = []
print()
print("Main Diagonal Elements:")
for i in range(n):
    for j in range(n):
        if i==j:
            print(matrix[i][j], end = " " )
            main_diagonal.append(matrix[i][j])

print()
print()
secondary_diagonal = []
print("Secondary Diagonal Elements:")
for i in range(n):
    for j in range(n):
        if i+j == n-1:
            print(matrix[i][j], end = " " )
            secondary_diagonal.append(matrix[i][j])

print()
print()


transpose = []
for row in range(n):
    list = []
    for column in range(n):
        list.append(0)
    transpose.append(list) 

print()
print("Transpose Matrix:")
for i in range(n):
    for j in range(n):
        print(matrix[j][i], end = " " )
        transpose[i][j] = (matrix[j][i])
    print()


# print("kjtgkjh")
# print(transpose)


# print(main_diagonal)
# print(secondary_diagonal)




final = []
for row in range(n):
    list = []
    for column in range(n):
        list.append(0)
    final.append(list) 


t_main = []
t_sec = []
                    
for i in range(n):
    for j in range(n):
        if i==j:
            t_main.append(transpose[i][j])
        if i+j == n-1:
            t_sec.append(transpose[i][j])    


# print(t_main)
# print(t_sec)



for i in range(n):
    for j in range(n):
        if i==j:
            final[i][j] = t_sec[j]
        elif i+j == n-1:
            final[i][j] = t_main[i] 

        else:
            final[i][j] = transpose[i][j]


print("Final Matrix After Diagonal Swapping:")

for i in range(n):
    for j in range(n):
        print(final[i][j], end = " " )
        
    print()