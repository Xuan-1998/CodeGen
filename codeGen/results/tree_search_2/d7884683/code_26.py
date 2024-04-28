import sys

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        dp = [0] * (n + 1)

        total_sum = sum(arr)
        left_sum = 0
        partitions = 0

        for i in range(n):
            if left_sum == total_sum - left_sum:
                partitions += 1
                left_sum = 0
            left_sum += arr[i]
            dp[i + 1] = max(partitions, dp[i])

        print(dp[n])

if __name__ == "__main__":
    solve()
