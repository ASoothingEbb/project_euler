#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#What is the 10 001st prime number?


#At some point I want to come back and understand the Meissel-Lehmer method, and create a really
#efficient algorithm for this, but today is not that day

#This is a sieve of Eratosthenes implementation

import primes

print(primes.nprimes(10001)[-1])
