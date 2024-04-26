def find_matching_indices():
    N = int(input())  # Read N from stdin
    Arr = list(map(int, input().split()))  # Read array elements

    matching_indices = {}  # Initialize empty dictionary
    for i in range(N):
        if Arr[i] == i + 1:  # Check if element at index i matches its value
            matching_indices[i + 1] = None  # Store the matching index (1-based) in the dictionary

    return list(matching_indices.keys())  # Return a list of keys as the output

print(find_matching_indices())
