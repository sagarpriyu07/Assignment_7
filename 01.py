month=int(input("Enter month number="))
match month:
    case month if month in (1,3,5,7,8,10,12):
        print("31 days")
    case month if month in (4,6,8,11):
        print("30 days")
    case 2:
        print("28 or 29 days")
    case _:
        print("Invalid month number")