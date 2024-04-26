def find_indices():
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Initialize an empty set to store the indices
    indices = set()
    
    for i in range(n):
        if arr[i] == i + 1:
            indices.add(i)
    
    return list(indices)

print(find_indices())
