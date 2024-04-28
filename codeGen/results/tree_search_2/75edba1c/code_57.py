def count_subarrays(Arr, K):
    n = len(Arr)
    dp = [0] * n  # Initialize a list to store the number of subarrays ending at each index i where max(Arr[i:]) > K

    for i in range(n):
        subarray_count = 0
        for j in range(i, -1, -1):  # Iterate from i to 0 (inclusive)
            if Arr[j] > K:
                subarray_count += 1
            else:
                break
        dp[i] = subarray_count

    return sum(dp)  # The number of contiguous subarrays where max(Arr[i:]) > K is the sum of all entries in the dp list

# Example usage:
N, K = map(int, input().split())
Arr = list(map(int, input().split()))
print(count_subarrays(Arr, K))
