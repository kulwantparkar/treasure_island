year = int(input("year:"))

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("it is a leap year")
        else:
            print("its not a leap year")
    else:
        print("it is a leap year")