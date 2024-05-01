import sys

n, m = map(int, input().split())
count = 0

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

greatest_common_divisor = gcd(n, m)

remaining_area = n * m - greatest_common_divisor ** 2

while remaining_area > 0:
    square_side = 1
    while True:
        if remaining_area >= square_side ** 2:
            break
        square_side += 1

    count += 1
    remaining_area -= square_side ** 2

print(count)
