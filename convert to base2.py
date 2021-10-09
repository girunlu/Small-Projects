def count_bits(num):
    n = num+1
    a = n/2
    y = 1
    while a > 2:
        a = a/2
        y += 1
    xnum = 0
    bin = ""
    num1 = 0
    for i in range (y,-1,-1):
        if xnum< num and (xnum+2**i)<num:
            xnum += 2**i
            bin += "1"
            num1 +=1
        elif xnum < num and (xnum+2**i)>num:
            bin+="0"
        elif xnum < num and (xnum+2**i)==num:
            bin+="1"
            xnum += 2**i
            num1 +=1
        elif xnum == num and (xnum+2**i)>num:
            bin+="0"
    bin = int(bin)
    return bin

while True:
    x = int(input("number to base 2 "))
    print(count_bits(x))
