def can_partition(arr, K, M):
    arr.sort()
    left = 0
    for right in range(len(arr)):
        while abs(arr[right] - arr[left]) > M and left < right:
            left += 1
        if right - left + 1 >= K:
            return True
    return False

N, K, M = map(int, input().split())
arr = list(map(int, input().split()))
print(can_partition(arr, K, M))
