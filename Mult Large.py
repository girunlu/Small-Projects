
def mult(a,b):
    a = str(a)
    b = str(b)

    a = a[::-1]
    b = b[::-1]

    num = ""
    elde = 0
    sum = 0
    ## düz mantık, eldeli çarpma işlemi, 3*5 = 15 elde var 1 gibi
    cnt = 0
    for s1,i in enumerate(b):
        for s2,l in enumerate(a):
            mult = int(l)*int(i)
            if len(str(mult))==2:   
              num+=str(elde+mult)[-1]
              elde = int(str(elde+mult)[0])
            else:
              if len(str(mult+elde))<2:
                    num+=str(mult+elde)
                    elde = 0
              else:
                    num+=str(mult+elde)[-1]
                    elde = int(str(mult+elde)[0])
              
        if (s1!=0 or s2!=0) or (len(str(a))<2 or len(str(b))<2):
            num+=str(elde)
        elde = 0
        num = num[::-1]+("0"*cnt)
        cnt+=1
        sum+=int(num)
        num = ""
    return str(sum)

while True:
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    print(mult(num1,num2))
    print(mult(num1,num2)==str(num1*num2))

