#The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
#Let us list the factors of the first seven triangle numbers:
#
# 1: 1
# 3: 1,3
# 6: 1,2,3,6
#10: 1,2,5,10
#15: 1,3,5,15
#21: 1,3,7,21
#28: 1,2,4,7,14,28
#We can see that 28 is the first triangle number to have over five divisors.
#
#What is the value of the first triangle number to have over five hundred divisors?

import math

def divisors(n):
    divs = []
    lim = int(math.sqrt(n))
    for i in range(1,lim+1): #for each divisor add it and its pair to the list
        if n % i == 0:      #e.g. 16 is divisible by 2, so add 2 and 8 as 2*8=16
            divs.append(i)
            divs.append(n/i)

    if divs[-1] == divs[-2]: #If n is square, the end will have 2 copies of the root
        divs = divs[:-1]    # e.g. 16 would be [2,8,4,4], if so remove the copy

    return divs

i = 1 #what number to add to get the next triangle number
tri = 0 #triangle number

while True: #keep counting divisors on successive triangle numbers till >500, then break and print it
    tri += i
    i += 1
    if(len(divisors(tri)) > 500):
            break

print(tri)

