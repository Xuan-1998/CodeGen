def max_partitions(arr):
    n = len(arr)
    dp = [[0] * (n // 2 + 1) for _ in range(n + 1)]

    total_sum = sum(arr)
    left_sum = 0

    for i in range(1, n + 1):
        left_sum += arr[i - 1]
        right_sum = total_sum - left_sum

        j = 0
        while j <= (n // 2) and left_sum >= arr[j]:
            if left_sum == right_sum:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            j += 1

    return dp[n][0]

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(max_partitions(arr))

if __name__ == "__main__":
    main()
