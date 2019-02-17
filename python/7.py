#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#What is the 10 001st prime number?


#At some point I want to come back and understand the Meissel-Lehmer method, and create a really
#efficient algorithm for this, but today is not that day

#This is a sieve of Eratosthenes implementation

import math

def n_primes(n):
    #so for simplicities sake im gunna create a single big array and sieve through it
    #how do I know how big to make the array?
    #you can approximate how big the nth prime is with n*(log n + log(log n))
    #and i'll just chuck on an extra 20% so that i never underestimate and can always
    #get away with never underestimating

    estimate = n * (math.log(n) + math.log( math.log(n))) * 1.2
    primes = []
    toSieve = range(estimate)
    toSieve[0] = -1
    toSieve[1] = -1
    i = 0
    
