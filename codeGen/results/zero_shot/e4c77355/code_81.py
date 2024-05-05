def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n  # Initialize lis with ones, as each element is a single-element subsequence

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    return max(lis)

# Read input from stdin
arr = list(map(int, input().split()))

# Calculate and print the length of the longest increasing subsequence
print(longest_increasing_subsequence(arr))
