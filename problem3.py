# Problem 3: Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the given number?
import math

num = int(input("enter athe number to find the greatest prime factor"))
grt = 0

while num%2 == 0:
    num /= 2
    if num > grt:
        grt = 2

for i in range(3, int(math.sqrt(num)+1),2):
    while num%i == 0:
        num = num/i
        if i > grt:
            grt = i

if num > 2:
    grt = num

print(grt)