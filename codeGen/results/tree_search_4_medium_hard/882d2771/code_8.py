import sys

def solve():
    t, l, r = map(int, input().split())
    memo = {2: 1}
    
    def f(n):
        if n not in memo:
            memo[n] = min(f(i) for i in range(l, n+1))
        return memo[n]
    
    print((t * sum(f(i) for i in range(l, r+1))) % (10**9 + 7))

if __name__ == "__main__":
    solve()
