import cmath
import random

a= random.choice(range(0,1000000000000))
b= random.choice(range(0,1000000000000))
c= random.choice(range(0,1000000000000))
d= (b**2) - (4*a*c)

root1= (-b +cmath.sqrt(d))/(2*a)
root2 = (-b -cmath.sqrt(d))/(2*a)
print("First root is "+  str(root1) +" "+ "second root is" + str(root2))


