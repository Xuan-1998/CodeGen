def partition_max_times(arr):
    n = len(arr)
    total_sum = sum(arr)

    dp = [[0] * (total_sum + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        left_sum = 0
        for j in range(i, -1, -1):
            left_sum += arr[j]
            if left_sum == total_sum // 2:
                dp[i][total_sum // 2] = max(dp[i-1][total_sum//2], dp[j-1][left_sum])
            elif left_sum < total_sum // 2 and i > j:
                dp[i][left_sum + (total_sum - left_sum) // 2] = max(
                    dp[i-1][left_sum + (total_sum - left_sum) // 2],
                    dp[j-1][left_sum]
                )

    return dp[n][total_sum // 2]

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(partition_max_times(arr))

if __name__ == "__main__":
    main()
