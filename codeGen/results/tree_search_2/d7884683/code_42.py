import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            if i % 2 == 0:
                mid = i // 2
                left_sum = sum(arr[:mid+1])
                right_sum = sum(arr[mid+1:])
                if left_sum == right_sum:
                    dp[i] = max(dp[i-1], dp[mid] + 1)
                else:
                    dp[i] = dp[i-1]
            else:
                mid = (i - 1) // 2
                left_sum = sum(arr[:mid+1])
                right_sum = sum(arr[mid+1:])
                if arr[mid] == left_sum and arr[mid] == right_sum:
                    dp[i] = max(dp[i-1], dp[mid] + 1)
                else:
                    dp[i] = dp[i-1]
        print(max(dp))

if __name__ == "__main__":
    solve()
