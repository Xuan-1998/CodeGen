import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
