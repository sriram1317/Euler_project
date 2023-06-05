# Problem 2: Even Fibonacci Numbers
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed n, find the sum of the even-valued terms.

pn = 1
fb = 1
sum = 0

num = int(input('Provide the number: '))

while (fb <= num):
    fn = pn + fb
    pn = fb
    fb = fn
    if fb%2 == 0:
        sum += fb
        
    
print(sum)