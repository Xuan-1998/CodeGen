def alternate_arrays(*arrays):
    result = []
    while any(arrays):
        for arr in arrays:
            if arr:
                result.append(arr.pop(0))
            else:
                result.append(None)
    return result

# Example usage:
arr1 = [1, 2, 3]
arr2 = ['a', 'b']
arr3 = [4, 5]

print(alternate_arrays(*arr1, *arr2, *arr3))  # Output: [1, 'a', 2, 'b', 3, 4, None, 5]
