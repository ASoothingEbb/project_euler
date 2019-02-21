#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


#The target number must be a multiple of the product of all primes from 1 to 20

#primes are: 1, 2, 3, 5, 7, 11, 13, 17, 19

factor = 1 * 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
multiplier = 0

#try a multiplier * factor until the result is divisible by all 1 to 20
divisible = False

while not divisible:
    multiplier += 1
    divisible = True
    the_num = factor * multiplier
    for i in range(1,21):
        if the_num % i != 0:
            divisible = False
            continue

print(factor*multiplier)

