year=int(input("Enter any year= "))
match year:
    case year if (year % 4== 0 and year%100!=0): 
        print("Non century Leap year")
    case year if (year % 100!= 0 and year%4!=0): 
        print("Non century Non Leap year")
    case year if (year%100==0 and year % 400!= 0): 
        print("Century Non Leap year")
    case year if (year%400==0 or year % 4== 0): 
        print("Century Leap year")
    