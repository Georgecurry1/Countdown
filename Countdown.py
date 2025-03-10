#functions

def countDown():
    countDownStart = int(input("enter the number you want to count down from: "))
    for i in range (countDownStart,0, -1):
        print(i)

def countUp():
    countUpStart = int(input("enter the number you want to count up to: "))
    for i in range (0,countUpStart, 1):
        print(i)





print("Hello User, do you want to set up a countdown or countup? Press 1 for countdown or 2 for countup: ")

choice = int(input())

if not choice == 1 or not choice == 2:
    while choice == 1 or not choice == 2:
        choice = int(input("Please input the correct value, 1 for countdown or 2 for count up: "))
    if choice == 1:
        countDown()
    elif choice == 2:
        countUp()
else:
    if choice == 1:
        countDown()    
    elif choice == 2:
        countUp()
        
