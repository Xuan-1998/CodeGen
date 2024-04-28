def count_subarrays(K, arr):
    n = len(arr)
    max_so_far = 0
    count = 0
    for i in range(n):
        if arr[i] > K:
            if arr[i] > max_so_far:
                max_so_far = arr[i]
                count += 1
    return count

K = int(input())
n = int(input())
arr = list(map(int, input().split()))
print(count_subarrays(K, arr))
