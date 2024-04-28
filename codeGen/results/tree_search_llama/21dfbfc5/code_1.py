def merge_arrays(*arrays):
    max_len = max(len(arr) for arr in arrays)
    result = []

    for i in range(max_len):
        for arr in arrays:
            if i < len(arr):
                result.append(arr[i])
            else:
                result.append(None)

    return result

# Example usage
array1 = [1, 2, 3]
array2 = ['a', 'b']
array3 = [True, False]

print(merge_arrays(array1, array2, array3))
