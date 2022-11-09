print("Choices")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplicaition")
print("4. Division")
choice=int(input("Your choice="))
match choice:
    case 1:
        a=int(input("Enter first number="))
        b=int(input("Enter second number="))
        print("Addition=",a+b)
    case 2:
        a=int(input("Enter first number="))
        b=int(input("Enter second number="))
        print("Subtraction=",a-b)
    case 3:
        a=int(input("Enter first number="))
        b=int(input("Enter second number="))
        print("Multiplication=",a*b)
    case 4:
        a=int(input("Enter first number="))
        b=int(input("Enter second number="))
        print("Division=",a/b)
    case _:
        print("Invalid choice")