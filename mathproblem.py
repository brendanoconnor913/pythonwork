import math
def is_prime(n):
    d = 2
    while d <= math.trunc(n**(1/2)):
        if n % d == 0:
            return d
        d += 1

primelist = [1,2,3,7,43]
prime = 1
for k in primelist:
    prime *= k

prime += 1

primeyon = is_prime(prime)
print(prime)
print(primeyon)

print(1807 / 13)
