name1 = input("type your name:").upper()
name2 = input("type your crush name:").upper()

name1_list = []
name2_list = []

for letter in name1:
    name1_list.append(letter)

for letter in name2:
    name2_list.append(letter)

list = name1_list + name2_list

# print(list)

T = []
R = []
U = []
E = []

L = []
O = []
V = []
E = []

for letter in list:
    if letter == "T":
        T.append(letter)

    if letter == "R":
        R.append(letter)

    if letter == "U":
        U.append(letter)

    if letter == "E":
        E.append(letter)

    if letter == "L":
        L.append(letter)

    if letter == "O":
        O.append(letter)

    if letter == "V":
        V.append(letter)

true = len(T) + len(R) + len(U) + len(E)
love = len(L) + len(O) + len(V) + len(E)

love_cal = true*10 + love
print(love_cal)

if love_cal < 10 or love_cal > 90:
    print(f"Your score is {love_cal}, you go together like coke and mentos.")
elif 40 < love_cal < 50:
    print(f"Your score is {love_cal}, you are alright together.")
else:
    print(f"Your score is {love_cal}.")