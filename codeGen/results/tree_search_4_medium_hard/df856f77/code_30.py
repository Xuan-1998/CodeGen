from sys import stdin
from functools import lru_cache

def solve():
    N = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))
    
    @lru_cache(None)
    def f(i):
        if i == 0:
            return 0
        res = float('inf')
        for k in range(i-1,-1,-1):
            if A[i] > A[k]:
                res = min(res, f(k) + 1)
        return res
    
    print(f(N-1))

if __name__ == "__main__":
    solve()
