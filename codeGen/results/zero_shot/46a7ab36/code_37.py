import sys
from math import factorial

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        total_words = factorial(n) // (factorial(n-m) * factorial(m-1))
        k = min(m-1, (n+1)//2 - 1)
        result = (total_words * 2**k) % (10**8 + 7)
        print(result)

if __name__ == "__main__":
    solve()
