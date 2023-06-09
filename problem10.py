# Problem 10: Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below n.
import math

def isPrime(n):
    if n > 2 and n % 2 == 0:
        return False

    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
sum = 0

n = int(input("Enter the number n: "))

num = 2
count = 0

while count < n - 2:
    if isPrime(num):
        sum += num
    num += 1
    count += 1
    

print(sum)