def can_reach_end(arr):
    n = len(arr)
    start = end = 0
    for i in range(n):
        if i >= end:
            start = i + 1
            end = i + arr[i]
        else:
            start = i + 1
        if end == n - 1:
            return True
    return False

n = int(input())
arr = list(map(int, input().split()))
print(can_reach_end(arr))
