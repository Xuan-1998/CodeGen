import sys

def max_partitions(arr):
    n = len(arr)
    left_sum = 0
    right_sum = sum(arr)
    partitions = 1
    dp = [0] * (n + 1)

    for i in range(1, n):
        left_sum += arr[i - 1]
        right_sum -= arr[i - 1]

        if left_sum == right_sum:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = max(dp[i - 1], 1)

    return dp[-1]


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(max_partitions(arr))


if __name__ == "__main__":
    main()
