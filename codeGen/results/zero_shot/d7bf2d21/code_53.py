def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    longest_lengths = set()
    for x in dp:
        if x not in longest_lengths:
            longest_lengths.add(x)
    return len(longest_lengths)

# Read input from stdin
arr = [int(x) for x in input().split()]

# Call the function and print the result to stdout
print(longest_increasing_subsequences(arr))
