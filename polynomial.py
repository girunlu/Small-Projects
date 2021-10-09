import matplotlib.pyplot as mpl
import random.randrange as rr
import random.choice as rch

## sign list for coefficients
sg = [-1,1]
## input
deg = int(input("Pol. Degree: "))

xs = []
## creating x points
for i in range(0,101):
    xs.append(-2+(4*i/100))

ys = []
for i in range(0,deg+1):
    sgn = rch(sg)
    coef = rr(1,11) # i kept it simple bcs interval wasnt determined, it is just random.
    cnt=0
    
    for pnt in xs:
        ##creating slots for every x value and assigning their value 
        if i == 0:
            ys.append(coef*sgn*(pnt**i))

        ## adding every individual value to its slot
        else:
            ys[cnt]+=(coef*sgn*(pnt**i))
            cnt+=1

## what i do here is, computing p's elements for every x for once and after that,
## summing the results so that i get y values for every x in the same polynomial 

mpl.plot(xs,ys)
mpl.show()
