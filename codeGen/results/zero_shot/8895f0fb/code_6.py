import sys
import itertools

def count_carries(n):
    carries = 0
    for i in range(10 ** n - 1, 10 ** n):
        for j in range(i + 1, 10 ** (n + 1)):
            carry = 0
            while i > 0 and j > 0:
                if (i % 10) + (j % 10) >= 10:
                    carry += 1
                    i //= 10
                    j //= 10
                else:
                    i %= 10
                    j %= 10
            carries += int(carry > 0)
    return carries / ((10 ** n - 1) * (10 ** (n + 1) - 10 ** n))

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(count_carries(n))
