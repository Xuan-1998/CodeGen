def max_partitions(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        left_sum = 0
        for j in range(i - 1, -1, -1):
            left_sum += arr[j]
            if left_sum == sum(arr[i:]):
                dp[i] = max(dp[i], dp[j - 1] + 1)
            elif left_sum > sum(arr[i:]):
                break

    return dp[n]

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(max_partitions(arr))

if __name__ == "__main__":
    main()
