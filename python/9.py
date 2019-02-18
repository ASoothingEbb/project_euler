#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
#a^2 + b^2 = c^2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.


import math

def findC():
    for b in range(1,1000): #for all possible a,b
        for a in range(1,1000):
            c2 = a**2 + b**2 #find sum of their squares
            c = math.sqrt(c2)
            if a + b + c == 1000: #a and b are integers, so can only be true if root of c2 is integer
                return a*b*c #if so we found it!
    return -1

print(findC())

