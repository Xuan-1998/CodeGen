import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        result = 0
        # Your logic here
        print(result % (10**9 + 7))
