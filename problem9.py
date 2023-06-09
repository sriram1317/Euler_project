# Problem 9: Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000. 
# Find the product abc such that a + b + c = n.


n = int( input("Enter the number m: "))
sum = 0
num = 1
for a in range(0,n):
    for b in range(a,n):
        c = n - a - b
        if c ** 2 == (a ** 2 + b **2):
            num = c*a*b

print(f'a={a}, b={b}, c={c}')
print(num)
