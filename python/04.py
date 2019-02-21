#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.


#Not the fastest, but an intuitive method
#Nested loops that check every 3x3 digit combination
#e.g. 999 * 999, 999*998, ....,  999*100, ...,  998*533, ...
#A palindrome can be checked by just seeing if the original is the same as the reverse
#So we just convert to string and check equality between the string and its reverse
#We do this for all 1,000,000 combinations and just keep track of the maximum

the_max = 0
for i in range(100,1000):
    for j in range(100,1000):
        product = i*j
        asString = str(product)
        if asString == asString[::-1]: #if string is the same backwards
            if product > the_max:
               the_max = product
print(the_max)
