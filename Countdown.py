#functions

def countDown():
    countDownStart = int(input("enter the number you want to cound down from?"))
    for i in range(0,countDownStart,-1):
        print(i)

def countUp():
    countDownStart = int(input("enter the number you want to cound down from?"))
    for i in range(0,countDownStart):
        print(i)





print("Hello User, do you want to set up a countdown or countup? Press 1 for countdown or 2 for countup ")

choice = int(input())

if choice == 1:
    countDown()

elif choice == 2:
    countUp()
else:
    choice = int(input("Please input the correct value, 1 for countdown or 2 for count up "))

