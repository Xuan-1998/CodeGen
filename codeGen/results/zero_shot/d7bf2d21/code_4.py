import sys

def find_lis_count(arr):
    n = len(arr)
    lis_count = [1] * n
    max_length = 1
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis_count[i] < lis_count[j] + 1:
                lis_count[i] = lis_count[j] + 1
        max_length = max(max_length, lis_count[i])
    
    return max_length

arr = list(map(int, input().split()))
print(find_lis_count(arr))
