# sum of two matrices



matrix1 = []
matrix2 =[]


row = int(input("Enter matrix row: "))
column = int(input("Enter matrix column: "))

print("\nFor matrix 1:")
for  i in range(row):
    rows = []
    for j in range(column):
        rows.append(int(input("Enter  element: ")))

    matrix1.append(rows)

# print(matrix1)


print("\nFor matrix 2: ")

for  i in range(row):
    rows = []
    for j in range(column):
        rows.append(int(input("Enter  element: ")))

    matrix2.append(rows)


# print(matrix2)   



result =[]
for i in range(row):
    res = []
    for j in range(column):
        res.append(matrix1[i][j] + matrix2[i][j])
    result.append(res)

# print(result) 

print("Sum Matrix is:")
for i in result:
    for j in i:
        print(j,end="\t")
    print()
               