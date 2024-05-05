import sys
input = sys.stdin.readline

def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    if a[0] <= b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

def solve(n):
    p = list(map(int, input().split()))
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    # Initialize base cases
    for i in range(2 * n + 1):
        if i < n:
            dp[i][0] = False
        else:
            dp[i][0] = True
        if i % 2 == 0:
            dp[0][i // 2] = True
        else:
            dp[0][i // 2] = False
    
    # Fill in the rest of the dp table based on the recurrence
    for i in range(1, n + 1):
        for j in range(i, 2 * n + 1):
            if p[i - 1] > max(p[:i]):
                dp[i][j] = dp[i - 1][max(range(i), key=lambda k: (p[k], k))]
            elif p[j // 2 - 1] < min(p[j // 2:j]):
                dp[i][j] = dp[max(0, i - 1)][min(range(j // 2, j), key=lambda k: (p[k], k))]
    
    # Check if dp[n][n] is true
    if dp[n][n]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        solve(n)
