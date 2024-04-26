def interleave(*arrays):
    result = []
    max_length = max(len(arr) for arr in arrays)
    
    for i in range(max_length):
        for arr in arrays:
            if i < len(arr):
                result.append(arr[i])
            else:
                result.append(None)
                
    return result

# Example usage:
input_arrays = [1, 2, 3], [4, 5, 6], [7, 8]
print(interleave(*input_arrays))  # Output: (1, 4, 7), (2, 5, 8)
