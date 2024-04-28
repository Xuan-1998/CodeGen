def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        prefix_sum = [0] * (n + 1)
        suffix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + arr[i]
        for i in range(n-1, -1, -1):
            suffix_sum[i] = sum(arr[i:])
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(i):
                if prefix_sum[i] == suffix_sum[j]:
                    dp[i] = max(dp[i], dp[j-1] + 1)
        print(max(dp))

if __name__ == '__main__':
    solve()
