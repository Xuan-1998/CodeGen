def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    dp = [[0] * (n + 1) for _ in range(2*n + 1)]
    
    def mergeable(a, j):
        if not a:
            return True
        for k in range(j):
            if a[k] in p[j:]:
                return False
        return True
    
    for i in range(2*n+1):
        if i < n:
            dp[i][i-n+1] = 1 if mergeable(p[:i], i) else 0
        elif i == 2*n:
            print("YES" if sum([dp[j][i-j] for j in range(i)]) == 1 else "NO")
        else:
            left = p[:min(i, n)]
            right = p[max(0, i-n+1):]
            if all(x not in y for x in left for y in right):
                dp[i][n] = 1 if all(dp[j][i-j] for j in range(i)) == 1 else 0
            print("YES" if dp[2*n][n] else "NO")

if __name__ == "__main__":
    solve()
