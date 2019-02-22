#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#What is the sum of the digits of the number 2^1000?


num = 2**1000
as_string = str(num)
the_sum=0
for c in as_string:
    the_sum += int(c)
print(the_sum)
