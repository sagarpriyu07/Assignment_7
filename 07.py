
x=int(input("Enter any number"))
match x:
    case x if x>0:
            print("Positive")
    case x if x<0:
            print("Negative")
    case x if x==0:
            print("Zero")
    case _:
        print("Invalid choice")