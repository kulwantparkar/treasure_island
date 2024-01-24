print("Welcome to treasure island.")

task_1 = input("There is two tunnel in front of you.Where want you go left or right?(l/r) ").lower()
if task_1 == "l":
    task_2 = input("You came to a lake.how you want to cross by boat or bridge?").lower()
    if task_2 == "boat":
        task_3 = input("Now you stand before 3 door red, blue and green.").lower()
        if task_3 == "red":
            print("its a trap. You have failed")
        elif task_3 == "green":
            print("its a trap. You have failed")
        elif task_3 == "blue":
            print("You have successfully found the trap.")
    else:
        print("its a trap. You have failed")
else:
    print("its a trap. You have failed")

