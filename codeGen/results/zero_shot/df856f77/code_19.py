def min_operations(arr):
    operations = 0
    i = 1

    while i < len(arr):
        if arr[i] <= arr[i-1]:
            j = i
            while j > 0 and arr[j] <= arr[j-1]:
                j -= 1
            operations += i - j
            i = j + 1
        else:
            i += 1

    return operations


# Read input from stdin
N = int(input())
arr = list(map(int, input().split()))

# Print output to stdout
print(min_operations(arr))
