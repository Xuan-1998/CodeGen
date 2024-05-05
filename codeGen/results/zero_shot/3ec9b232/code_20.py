n = int(input())
m = list(map(int, input().split()))

def get_permutations(arr):
    if len(arr) == 1:
        return [arr]
    result = []
    for i in range(len(arr)):
        pivot = arr[i]
        rest = arr[:i] + arr[i+1:]
        for p in get_permutations(rest):
            result.append([pivot] + p)
    return result

def merge_into_sorted(arr):
    result = []
    while arr:
        min_val = float('inf')
        for i in range(len(arr)):
            if arr[i] < min_val:
                min_val = arr[i]
        result.append(min_val)
        arr.remove(min_val)
    return result

permutations = get_permutations(m)
count = 0
for p in permutations:
    if merge_into_sorted(p) == m:
        count += 1

print(count % (10**9 + 7))
