# Problem 6: Sum square difference
# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square 
# of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.

num = int(input("Provide the number: "))

sumSquared = 0
sumNum = 0

for i in range(1,num+1):
    sumSquared += (i*i)
    sumNum += i
    
sumNum *= sumNum
diff = sumNum - sumSquared

print(diff)