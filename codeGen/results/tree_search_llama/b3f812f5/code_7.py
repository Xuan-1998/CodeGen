def find_equal_indices():
    n = int(input())
    arr = list(map(int, input().split()))
    
    equal_indices = {}
    
    for i in range(n):
        if arr[i] == i + 1:
            equal_indices[i + 1] = None
    
    return sorted(list(equal_indices.keys()))

print(find_equal_indices())
