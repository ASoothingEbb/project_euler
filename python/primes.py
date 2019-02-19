import math
def primes_under(n):
    primes = []
    nums = list(range(n))
    nums[0] = -1
    nums[1] = -1
    i = 0
    j = 0
    while i < n:
        while nums[i] != -1:
            j = i
            prime = j
            primes.append(prime)
            while j < n:
                nums[j] = -1
                j += prime
            j = prime
        i += 1
    return primes

def nprimes(n):
    # n = x/ln(x)
    # x = n log n + n log log n 
    return primes_under(int((n*math.log(n) + math.log(math.log(n)))*1.5))[:n]
