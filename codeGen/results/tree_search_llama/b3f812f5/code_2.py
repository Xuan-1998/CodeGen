def find_indices(arr):
    arr.sort(key=lambda x: (x[0], x[1]))
    result = []
    for i in range(len(arr)):
        if arr[i][0] == arr[i][1]:
            result.append(i+1)
    return result

N = int(input())
arr = [int(x) for x in input().split()]
print(find_indices([(x, i+1) for i, x in enumerate(arr)]))
