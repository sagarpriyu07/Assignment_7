s= input("Enter a string :")
s=s.strip()
match s:
    case s if ' ' in s:
        print("Multiword string")
    case s if ' ' not in s:
        print("Single word string") 