import sys

def merge(a, b):
    result = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    result.extend(a)
    result.extend(b)
    return result

def solve(n, p):
    dp = [[False for _ in range(n+1)] for _ in range(2*n+1)]

    for i in range(2*n+1):
        if i == 0:
            dp[i][0] = True
        elif i == 2*n:
            for j in range(n+1):
                dp[i][j] = False
        else:
            for j in range(n+1):
                if i < n and p[i-1] > p[n-1]:
                    dp[i][j] = dp[i-1][j+1]
                elif i >= n and p[2*n-1-i] > p[n-1]:
                    dp[i][j] = dp[2*n-1-i][j+1]
                else:
                    if j == 0:
                        for k in range(2*n+1):
                            if i < k and p[k-1] > p[n-1]:
                                dp[i][j] = dp[i][0] and (k >= n or p[k-1] > p[2*n-1-k])
                    else:
                        dp[i][j] = dp[i-1][j+1]

    for j in range(n+1):
        if not any(dp[i][j] for i in range(2*n+1)):
            return "NO"
    return "YES"

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        print(solve(n, p))

if __name__ == "__main__":
    main()
