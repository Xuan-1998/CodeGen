import sys
from functools import lru_cache

def solution():
    T = int(input())
    for _ in range(T):
        n = int(input())
        probs = [list(map(int, input().split())) for _ in range(n)]
        
        @lru_cache(None)
        def dp(i, mask):
            if i == n:
                return 1
            p0, num0, num1 = probs[i]
            p = (p0 / 100) * (mask & (1 << num0)) + (1 - p0) * (mask & (1 << num1))
            return p * dp(i+1, mask | ((p > 0.5) << min(num0, num1)))

        print(round(dp(0, 0), 6))

if __name__ == "__main__":
    solution()
