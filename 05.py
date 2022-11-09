n=int(input("Enter any number:"))
match n:
    case n if n%2==0:
        print("Saurabh Shukla")
    case n if n%2!=0 and n<0:
        print("Prateek Jain")
    case n if n%2!=0 and n>0:
        print("Aditya Choudhary")