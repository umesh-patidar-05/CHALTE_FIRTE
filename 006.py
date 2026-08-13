'''
Assignment: Student Result Analyzer

Ek Python program banao jo user se 5 subjects ke marks input le.

Requirements:
5 subjects ke marks input lo.
Har subject ke marks ke basis par check karo:
90–100 → Grade A
75–89 → Grade B
60–74 → Grade C
40–59 → Grade D
0–39 → Fail
Total marks calculate karo.
Percentage calculate karo.
Overall result:
Agar kisi bhi subject me marks 40 se kam hain → Fail
Otherwise → Pass
Percentage ke basis par overall category batao:
90+ → Excellent
75–89 → Very Good
60–74 → Good
40–59 → Average
Program ke end me:
Total marks
Percentage
Pass/Fail
Category
Har subject ka grade

Conditions

input() use karo
if / elif / else use karo
at least one loop use karo
Arithmetic operators use karo
Comparison operators use karo
Logical operators use karo
List, function, dictionary abhi use mat karna
Internet se solution mat dekhna 😄
Example

Input:

Enter marks of subject 1: 85
Enter marks of subject 2: 72
Enter marks of subject 3: 91
Enter marks of subject 4: 68
Enter marks of subject 5: 80

Expected type of output:

Total Marks: ...
Percentage: ...
Result: Pass
Category: Very Good

Subject 1: B
Subject 2: C
Subject 3: A
Subject 4: C
Subject 5: B
'''





marks = []
for i in range(5):
    m = int(input(f"Enter marks of subject {i+1}: "))
    marks.append(m)


marks1 = marks[0]
marks2 = marks[1]
marks3 = marks[2]
marks4 = marks[3]
marks5 = marks[4]



def grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 40:
        return "D"

    else:
        return "Fail"


total_marks = marks1 + marks2 + marks3 + marks4 + marks5

percentage = total_marks / 5

if marks1 >=40 and marks2 >=40 and marks3 >=40 and marks4 >=40 and marks5 >=40:
    result = "Pass"

else:
    result = "Fail"    


if percentage >=90:
    category = "Excellent"

elif percentage >= 75:
    category = "Very Good"

elif percentage >=60:
    category = "Good"

elif percentage >=40:
    category = "Average"            



print()
print("Total marks: ", total_marks)
print("Percentage: ", percentage)
print("Result: ", result)
print("Category: ", category)
print()
print("Subject 1: ", grade(marks1))
print("Subject 2: ", grade(marks2))
print("Subject 3: ", grade(marks3))
print("Subject 4: ", grade(marks4))
print("Subject 5: ", grade(marks5))