import random
import time

x = random.randint(1,20)

num = 0
cnt = 0
while num != x:
    num = int(input("guess the number "))
    if num < x:
        print("it's lower than the number ")
        cnt += 1
    elif num > x:
        print("it's higher than the number ")
        cnt += 1
    else:
        print("congrats, u won at", cnt ,"time")
        time.sleep(3)

