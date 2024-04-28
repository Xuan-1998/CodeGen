def partition_count(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        left_sum = right_sum = 0
        for j in range(i - 1, -1, -1):
            left_sum += arr[j]
            if left_sum == right_sum:
                dp[i] = max(dp[i], dp[j - 1] + 1)
            elif left_sum > right_sum:
                right_sum = left_sum
        for k in range(i, n):
            right_sum += arr[k]
            if left_sum == right_sum:
                dp[i] = max(dp[i], dp[k] + 1)

    return dp[-1]

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(partition_count(arr))

if __name__ == "__main__":
    main()
