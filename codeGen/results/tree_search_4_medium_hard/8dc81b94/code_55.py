import sys

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[False] * (n+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][i] = all(x == 0 for x in arr[i:i+1])

    for length in range(2, n+1):
        for start in range(n-length+1):
            end = start + length
            if all(x == 0 for x in arr[start:end]):
                dp[start][end] = True
            else:
                dp[start][end] = (dp[start][start+length-1] or 
                                   dp[end-length][end])

    print("YES" if any(dp[0][i] for i in range(n+1)) else "NO")

if __name__ == "__main__":
    solve()
