from sys import stdin
from functools import lru_cache

def solve():
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    
    @lru_cache(None)
    def dp(i):
        if i < 0:
            return "NO"
        if all(x == 0 for x in arr[i:]):
            return "YES"
        if any(x > 0 for x in arr[:i+1]):
            return min(dp(i-1), dp(-1))
        return "NO"

    print("YES" if dp(n-1) == "YES" else "NO")

if __name__ == "__main__":
    solve()
