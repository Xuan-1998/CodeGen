import sys

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        dp = {}
        seen = {}

        def dfs(n, prev_val):
            if (n, prev_val) in dp:
                return dp[(n, prev_val)]
            if n < 1 or n > 2 * 10**5:
                return False
            if not seen.get(prev_val, False):
                seen[prev_val] = True
                dp[(n, prev_val)] = any(dfs(n - (b[i] - prev_val), b[i]) for i in range(1, n))
                return dp[(n, prev_val)]
            return False

        if dfs(n, 0):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
