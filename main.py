height = int(input("type your height in cm:"))
total = 0
if height > 120:
    age = int(input("type your age:"))
    if age < 12:
        total = 5
    elif age<18:
        total = 7
    elif 45<age and age<55:
        total = 0
    else:
        total = 12

    photo = input("do you want picture.(y/n):").lower()

    if photo == "y":
        print(f"your total is ${total + 3}")
    else:
        print(f"your total is ${total}")

else:
    print("you can't ride")




