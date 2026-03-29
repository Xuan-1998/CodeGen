from sys import stdin

def can_reach_last(arr):
    n = len(arr)
    dp = [False] * (n + 1)

    # Initialize dp[0] as True since we can always reach the start
    dp[0] = True

    for i in range(1, n + 1):
        if dp[i - 1]:
            if i + arr[i - 1] >= n:
                dp[i] = True

    return dp[-1]

if __name__ == "__main__":
    arr = list(map(int, stdin.readline().split()))
    print(can_reach_last(arr))
