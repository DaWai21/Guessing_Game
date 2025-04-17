import random
low = 1
high = 100

ans = random.randint(low , high )
while True:
    user = int(input("Enter the number between 1 and 100: "))
    if user > ans:
        print("Too high")
    elif user < ans:
        print("Too low")

    else:
        print("bingo")
        break