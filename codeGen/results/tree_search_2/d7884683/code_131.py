def max_partitioning(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i:])

        if left_sum == right_sum:
            j = i - 1
            dp[i] = max(dp[j-1] + 1, i-j+1) if j >= 0 else i-j+1
        else:
            dp[i] = dp[i-1]

    return dp[-1]

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(max_partitioning(arr))

if __name__ == "__main__":
    main()
