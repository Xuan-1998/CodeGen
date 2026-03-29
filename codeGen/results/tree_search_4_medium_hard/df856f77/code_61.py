def min_operations(arr):
    n = len(arr)
    dp = [0] * n
    prev_value = float('-inf')

    for i in range(n):
        if arr[i] <= prev_value:
            dp[i] = 1 + dp[i-1] if i > 0 else 1
        else:
            dp[i] = dp[i-1] if i > 0 else 0
        prev_value = arr[i]

    return sum(dp)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(min_operations(arr))
