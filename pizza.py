print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L:").upper()  # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N:").upper() # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N:").upper() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# Thank you for choosing Python Pizza Deliveries!
# Your final bill is: $28.
bill = 0
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if add_pepperoni == "Y":
    bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Thank you for choosing Python Pizza Deliveries!Your final bill is: ${bill}.")