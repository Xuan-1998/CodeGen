def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [1] * n  # Initialize DP array with all 1s

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_length = max(dp)  # Find the maximum length of increasing subsequences
    count = sum(1 for x in dp if x == max_length)  # Count the number of such subsequences

    return count

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(longest_increasing_subsequences(arr))
