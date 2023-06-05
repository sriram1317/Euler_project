# Problem 4: Largest palindrome product
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two n-digit numbers.
import math

num = int(input("enter the number"))
largestNum = int(math.pow(10, num) - 1)
smallestNum = int(math.pow(10, (num - 1)))
largestPall = 0

def pallindrome(x):
    numStr = str(x)
    return numStr == numStr[::-1]

for i in range(largestNum, smallestNum, -1):
    for j in range(i, smallestNum, -1):
        num = i * j
        if(pallindrome(num) and num > largestPall):
            largestPall = num
            if j > smallestNum:
                smallestNum = j
            break

print(largestPall)
