#functions

def countDown():
    countDownStart = input("enter the number you want to count down from?")
    for i in range(int(countDownStart),0 -1):
        print(i)

def countUp():
    countUpStart = input("enter the number you want to count up from?")
    for i in range(0,int(countUpStart), 1):
        print(i)





print("Hello User, do you want to set up a countdown or countup? Press 1 for countdown or 2 for countup ")

choice = int(input())

if choice == 1:
    countDown()

elif choice == 2:
    countUp()
else:
    choice = int(input("Please input the correct value, 1 for countdown or 2 for count up "))

