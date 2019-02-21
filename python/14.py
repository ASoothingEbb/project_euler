#The following iterative sequence is defined for the set of positive integers:
#
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#
#Using the rule above and starting with 13, we generate the following sequence:
#
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
#Which starting number, under one million, produces the longest chain?
#
#NOTE: Once the chain starts the terms are allowed to go above one million.

def do_collatz(n): #return a reversed collatz sequence from 1 -> n, e.g. 1,2,4,8,16,5
    if n == 0:
        return 0
    seq = []
    while n != 1:
        seq.append(int(n))
        if n%2 == 0:
            n /= 2
        else:
            n = 3*n+1
    seq.append(1)
    return seq[::-1]




the_limit = 1000000 #counting down from
collatz_length = {} #dict to store all collatz lengths
i = the_limit - 1 #starting n
while i > 0: #while we haven't found collatz lengths for all numbers
    if collatz_length.get(i,-1) == -1: #if we have no length for this number
        seq = do_collatz(i)            #work out the sequence
        for j in range(len(seq)):      #then for all numbers in the sequence returned
            collatz_length[seq[j]] = j #record their sequence distance from 1, this means for if we do collatz 5, "5,16,8,4,2,1" 
                                       #we wouldnt need to run 16 and 8 as we worked them out here, so less computations
    i -= 1

print(sorted(collatz_length, key = collatz_length.get, reverse=True)[0]) #sort the hashmap by value descending and take the first item, i.e. the biggest



