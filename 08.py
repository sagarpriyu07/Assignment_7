s1= input("Enter first string")
s2= input("Enter second string")
match (s1,s2):
    case (s1,s2) if s1==s2:
        print("Identical string")
    case (s1,s2) if s1<s2:
        print("First comes before second ")
    case (s1,s2) if s1>s2:
        print("Second comes before first")