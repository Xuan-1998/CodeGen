import sys

def count_subarrays(arr, K):
    n = len(arr)
    max_val = 0
    count = 0
    for i in range(n):
        if arr[i] > K:
            max_val = arr[i]
            count += 1
        else:
            while max_val > K and i < n-1:
                max_val = max(max_val, arr[i+1])
                i += 1
    return count

n, K = map(int, input().split())
arr = list(map(int, input().split()))
print(count_subarrays(arr, K))
