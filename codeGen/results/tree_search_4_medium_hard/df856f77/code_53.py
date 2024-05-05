def min_operations():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * (n + 1)

    for i in range(1, n):
        prev_increasing_idx = -1
        for j in range(i):
            if arr[j] < arr[i]:
                prev_increasing_idx = j
                break
        if prev_increasing_idx == -1:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = min(dp[i-1], i - prev_increasing_idx) + (arr[i] - arr[prev_increasing_idx])

    print(dp[-1])

if __name__ == "__main__":
    min_operations()
