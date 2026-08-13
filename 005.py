# FIND GREATER NUMBER OUT OF 4 NUMBERS




a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a > b:

    if a > c:

        if a > d:
            print(f"{a} is greater")

        else:
            print(f"{d} is greater")

    else:

        if c > d:
            print(f"{c} is greater")

        else:
            print(f"{d} is greater")    

elif b > c:

    if b > d:
        print(f"{b} is greater") 

    else:
        print(f"{d} is greater")
                    

else:

    if c > d:
        print(f"{c} is greater") 

    else:
        print(f"{d} is greater")