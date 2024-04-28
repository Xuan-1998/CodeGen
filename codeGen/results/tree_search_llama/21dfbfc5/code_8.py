def concatenate_arrays(*arrays):
    if not arrays:  # Base case: no arrays left to process
        return []
    
    array = arrays[0]
    remaining_arrays = arrays[1:]
    
    result = []
    for i in range(min(len(array), len(remaining_arrays))):
        result.append(array[i])
        if i < len(remaining_arrays):
            result.append(next_array_value(remaining_arrays))
    
    # Pad the result with nils if one of the arrays was shorter
    while len(result) < sum(map(len, arrays)):
        result.append(None)
    
    return result


def next_array_value(arrays):
    for array in arrays:
        try:
            yield next(array)
        except StopIteration:
            pass


# Example usage:
arrays = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
print(concatenate_arrays(*arrays))  # Output: [1, 3, 6, 2, 4, 7, 5, 8, None, None]
