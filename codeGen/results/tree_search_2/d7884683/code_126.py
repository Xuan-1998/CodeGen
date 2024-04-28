import sys

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        total_sum = sum(arr)
        if total_sum % 2 != 0:
            print(0)
            continue
        dp = [0] * (n + 1)
        for i in range(n):
            if (total_sum - sum(arr[:i+1])) % 2 == 0 and (sum(arr[i:])) % 2 == 0:
                dp[i+1] = max(dp[i+1], dp[i] + 1)
            else:
                dp[i+1] = dp[i]
        print(dp[-1])

if __name__ == "__main__":
    solve()
