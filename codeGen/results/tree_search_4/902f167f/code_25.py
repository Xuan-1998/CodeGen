import sys
from math import gcd

def find_min_squares(n, m):
    def gcd_of_two(a, b):
        while b:
            a, b = b, a % b
        return a
    
    lcm = n * m // gcd(n, m)
    min_squares = 0
    i = 1
    while i * i <= lcm:
        if lcm % (i * i) == 0:
            min_squares += lcm // (i * i)
            break
        i += 1

    return min_squares

n, m = map(int, input().split())
print(find_min_squares(n, m))
