def min_operations(arr):
    n = len(arr)
    sorted_arr = sorted(arr)

    operations = 0
    for i in range(n):
        if arr[i] != sorted_arr[i]:
            operations += 1

    return operations

n = int(input())
arr = list(map(int, input().split()))
print(min_operations(arr))
