import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        memo = {0: 1}
        def dp(k):
            if k not in memo:
                digits = [int(d) + 1 for d in str(n)]
                memo[k] = len(''.join(map(str, digits)))
            return memo[k]
        print((dp(m)) % (10**9 + 7))

if __name__ == "__main__":
    solve()
