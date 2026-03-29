def min_operations(arr):
    n = len(arr)
    operations = 0
    
    for i in range(n-1):
        if arr[i] >= arr[i+1]:
            diff = arr[i] - arr[i+1] + 1
            operations += diff
            arr[i+1] = arr[i] + 1
            
    return operations

n = int(input())
arr = list(map(int, input().split()))
print(min_operations(arr))
