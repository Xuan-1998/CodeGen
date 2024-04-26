def recursive_sort(arr, x):
    if x == len(arr) - 1:
        return arr
    else:
        arr[x], arr[x-1] = arr[x-1], arr[x]
        return recursive_sort(arr, x-1)

n = int(input())
permutation = list(range(1, n+1))
for i in range(n):
    permutation = recursive_sort(permutation, i)
print(" ".join(map(str, permutation)))
