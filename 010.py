# matirx mutiplication:


r1 = int(input("Enter row for first matrix: "))
c1 = int(input("Enter column for first matrix: "))

matrix1 =[]
print("\nEnter matrix1: ")
for  i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input("Enter  element: ")))

    matrix1.append(row)


r2 = int(input("\nEnter row for second matrix: "))
c2 = int(input("Enter column for second matrix: "))

matrix2 =[]
print("\nEnter matrix2: ")
for  i in range(r2):
    row = []
    for j in range(c2):
        row.append(int(input("Enter  element: ")))

    matrix2.append(row)



if c1 == r2:

    result = []

    # METHOD 1:
    # for i in range(r1):
    #     row = []
    #     for j in range(c2):
    #         row.append(0)
    #     result.append(row)

    # for i in range(r1):
    #     for j in range(c2):    
    #         for k in range(c1):
    #             result[i][j] += matrix1[i][k] * matrix2[k][j] 

    # METHOD 2:
    for i in range(r1):
        row= []
        for j in range(c2):
            sum = 0    
            for k in range(c1):
                sum +=  matrix1[i][k] * matrix2[k][j] 
            row.append(sum)
        result.append(row)


          
      
    print("\nMatrix1: ")
    for i in matrix1:
        for j in i:
            print(j,end="\t")
        print()

    print("\nMatrix2: ")
    for i in matrix2:
        for j in i:
            print(j,end="\t")
        print()
                        
    print("\nResult: ")
    for i in result:
        for j in i:
            print(j,end="\t")
        print()

 
else:
    print("\nMatrix multiplication is not possible..........")







# Enter row for first matrix: 2
# Enter column for first matrix: 3

# Enter matrix1: 
# Enter  element: 1
# Enter  element: 2
# Enter  element: 3
# Enter  element: 4
# Enter  element: 5
# Enter  element: 6

# Enter row for second matrix: 3
# Enter column for second matrix: 2

# Enter matrix2: 
# Enter  element: 6
# Enter  element: 5
# Enter  element: 4
# Enter  element: 3
# Enter  element: 2
# Enter  element: 1

# Matrix1: 
# 1       2       3
# 4       5       6

# Matrix2: 
# 6       5
# 4       3
# 2       1

# Result: 
# 20      14
# 56      41