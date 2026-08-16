'''
3-D matrix

2-class
 3-student
    5-subject
'''





data =[]
for i in range(2):
    row1 =[]
    for j in range(3):
        row2 = []
        print(f"Enter Class{i+1} Student{j+1} subjects name: ")
        for k in range(5):
            row2.append(input("Enter subject: "))

        row1.append(row2)
    data.append(row1)

# print(data)  

for i in range(len(data)):
    print(f"class{i+1}: ")
    for j in range(len(data[i])):
        print(f"  student{j+1}:--->", end="  ")
        for k in range(len(data[i][j])):
            print(data[i][j][k],end=", ")
        print()    
    print()    





# Enter Class1 Student1 subjects name: 
# Enter subject: math 
# Enter subject: physics
# Enter subject: python
# Enter subject: dbms
# Enter subject: aptitude
# Enter Class1 Student2 subjects name: 
# Enter subject: math    
# Enter subject: physics
# Enter subject: python
# Enter subject: dbms
# Enter subject: aptitude
# Enter Class1 Student3 subjects name: 
# Enter subject: math
# Enter subject: physics
# Enter subject: python
# Enter subject: dbms
# Enter subject: aptitude
# Enter Class2 Student1 subjects name: 
# Enter subject: math
# Enter subject: physics
# Enter subject: python
# Enter subject: dbms
# Enter subject: aptitude
# Enter Class2 Student2 subjects name: 
# Enter subject: math
# Enter subject: physics
# Enter subject: python
# Enter subject: dbms
# Enter subject: aptitude
# Enter Class2 Student3 subjects name: 
# Enter subject: math
# Enter subject: physics
# Enter subject: python
# Enter subject: dbms
# Enter subject: aptitude
# class1: 
#   student1:--->  math, physics, python, dbms, aptitude, 
#   student2:--->  math, physics, python, dbms, aptitude, 
#   student3:--->  math, physics, python, dbms, aptitude, 

# class2: 
#   student1:--->  math, physics, python, dbms, aptitude, 
#   student2:--->  math, physics, python, dbms, aptitude, 
#   student3:--->  math, physics, python, dbms, aptitude,     