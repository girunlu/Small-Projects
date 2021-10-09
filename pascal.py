
def pascal(alist):
    blist =[]
    curr = alist[1]
    blist.append(alist[0])
    for nxt in alist:
        blist.append(curr+nxt)
        curr = nxt
       
    blist.pop(1)
    blist.append(alist[-1])
    return blist

def ptri(step, list):
    a = 1
    trilist=[]
    while a < step:
        list = pascal(list)
        trilist.append(list)
        a+=1
    return trilist

while True:
    num = int(input("enter iteration number "))
    lst = []
 
    num_ele = int(input("enter number of elements "))
    for i in range(0, num_ele):
        ele = int(input())
        lst.append(ele)

    LIST = [lst]+ptri(num,lst)

    for i in LIST:
        print(i, '')


