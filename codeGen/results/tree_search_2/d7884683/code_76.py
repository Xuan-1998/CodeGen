from sys import stdin

def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        arr = list(map(int, stdin.readline().split()))
        dp = [0] * (n + 1)
        left_sum = 0
        right_sum = sum(arr)
        for i in range(n - 1, -1, -1):
            if i % 2 == 0:
                left_sum += arr[i]
            else:
                right_sum -= arr[i]
            dp[i] = (left_sum == right_sum) + max(dp[i+1], dp[i-1])
        print(max(dp))

solve()
