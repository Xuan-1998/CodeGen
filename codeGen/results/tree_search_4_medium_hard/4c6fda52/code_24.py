import sys

def min_changes(s, k):
    n = len(s)
    dp = [[0] * (k+1) for _ in range(n+1)]

    # Fill the first row of dp array
    for j in range(1, k+1):
        if s[j-1] == 'R':
            dp[0][j] = 1
        elif s[j-1] == 'G':
            dp[0][j] = 2
        else:
            dp[0][j] = 3

    # Fill the rest of the dp array
    for i in range(1, n+1):
        for j in range(1, min(i+1, k)+1):
            if s[i-1] == 'R':
                dp[i][j] = dp[i-1][j-1] + 1
            elif s[i-1] == 'G':
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + 1

    return dp[n-k][k]

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()
        print(min_changes(s, k))

if __name__ == "__main__":
    main()

