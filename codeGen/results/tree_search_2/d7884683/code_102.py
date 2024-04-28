from sys import stdin

def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        arr = list(map(int, stdin.readline().split()))
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1, n+1):
            j = i-1
            while j >= 0:
                if sum(arr[:j+1]) == sum(arr[j+1:i+1]):
                    break
                j -= 1
            dp[i] = max(dp[j] + (dp[i-j-1] if j > 0 else 0), 0)
        print(dp[-1])

solve()
