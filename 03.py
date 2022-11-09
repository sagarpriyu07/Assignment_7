print("Choices")
print("1. Check whtther a given set of three numbers are lengths of an isosceles triangle or not.")
print("2. Check whtther a given set of three numbers are lengths of sides of right angled triangle or not.")
print("3. Check whtther a given set of three numbers are lengths of an equilateral triangle or not.")
print("4. Exit")
n=int(input("Your choice="))
match n:
    case 1:
        a=int(input("Enter first side="))
        b=int(input("Enter second side="))
        c=int(input("Enter third side=")) 
        if (a==b and b!=c) or (a==c and b!=c) or (b==c and c!=a):
            print("Isoscles triangle ")
        else:
            print("Not an isoscles triangle")
    case 2:
        a=int(input("Enter first side="))
        b=int(input("Enter second side="))
        c=int(input("Enter third side="))
        if (a**2==b**2+c**2) or (b**2==a**2+c**2) or (c**2==b**2+a**2) :
            print("Right angled triangle ")
        else:
            print("Not an Right angled triangle")
    case 3:
        a=int(input("Enter first side="))
        b=int(input("Enter second side="))
        c=int(input("Enter third side="))
        if a==b==c:
            print("Equilateral triangle ")
        else:
            print("Not an Equilateral triangle")
    case 4:
        exit()
    case _:
        print("Invalid choice")
