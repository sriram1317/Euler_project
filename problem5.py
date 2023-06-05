# Problem 5: Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?

#Solution: find lowest common multiple from 1 to n and print the maximum LCM


num = int(input("enter te number: "))
maxLcm = 1

def lcm(a, b):
    return int((a * b) / gcd(a, b))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
for i in range(1,num+1):
    maxLcm = lcm(maxLcm, i)

print(maxLcm)
