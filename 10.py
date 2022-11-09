s1=input("What is your favourite color ? ")
l1=["yellow","blue","orange","white","black","red"]
for color in l1:
    if color in s1:
        c=color
        break
else:
    c="other"
match c:
    case "yellow":
        print("Monday")
    case "blue":
        print("Tuesday")
    case "orange":
        print("Wednesday")
    case "white":
        print("Thrusday")
    case "black":
        print("Friday")
    case "red":
        print("Saturday")
    case "other":
        print("Sunday")
    