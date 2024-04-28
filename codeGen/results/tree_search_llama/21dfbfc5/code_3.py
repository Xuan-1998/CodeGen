def merge_arrays(*arrays):
    result = []
    indices = [0] * len(arrays)
    
    while any(index < len(array) for array in arrays for index in indices):
        for i, array in enumerate(arrays):
            if indices[i] < len(array):
                result.append(array[indices[i]])
                indices[i] += 1
                break
        
        # If all arrays have been exhausted, add nils to the result
        if all(index >= len(array) for array in arrays):
            break
    
    return result

# Test the function
arrays = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(merge_arrays(*arrays))
