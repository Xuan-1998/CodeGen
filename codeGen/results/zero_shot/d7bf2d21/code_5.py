def lis_length(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp array with ones

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp

def find_longest_lis_length(arr):
    dp = lis_length(arr)
    max_lis_length = max(dp)

    return max_lis_length

def count_longest_lis(arr):
    max_lis_length = find_longest_lis_length(arr)
    count = 0

    for i in range(len(arr)):
        if lis_length(arr[:i+1]) == max_lis_length:
            count += 1

    return count

arr = list(map(int, input().split()))
print(count_longest_lis(arr))
