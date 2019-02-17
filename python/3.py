#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?


#This is not the fastest method but it is intuitive
#We just keep trying to divide the number by an incrementing factor
#when we've gotten to 0 we know that the last number we divided
#by was the biggest factor

the_number = 600851475143

current = 1
while the_number != 1:
    current += 1
    while the_number % current == 0:
        the_number /= current

print(current)
