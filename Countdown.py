#hello
print("Hello User, do you want to set up a countdown or countup? Press 1 for countdown or 2 for countup ")

choice = int(input())

if choice == 1:
    print("user chose 1")
elif choice == 2:
    print("user chose 2")
else:
    choice = input("Please input the correct value, 1 for countdown or 2 for count up ")