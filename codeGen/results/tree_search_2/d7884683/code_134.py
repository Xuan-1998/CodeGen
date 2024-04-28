def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        dp = {0: 0}
        for i in range(1, n+1):
            if sum(arr[:i]) == sum(arr[i:]):
                dp[i] = max(dp.get(i-1, 0), 1 + dp.get((i-1)//2, 0))
            else:
                dp[i] = dp.get(i-1, 0)
        print(dp[n])

if __name__ == '__main__':
    solve()
