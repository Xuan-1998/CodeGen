def min_operations(arr):
    n = len(arr)
    ops = 0
    
    for i in range(n-1):
        # If current element is not less than next, we need to reduce it
        while arr[i] >= arr[i+1]:
            arr[i] -= 1
            ops += 1
    
    return ops

n = int(input())
arr = list(map(int, input().split()))
print(min_operations(arr))
