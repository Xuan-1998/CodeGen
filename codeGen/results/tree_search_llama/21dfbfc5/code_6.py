def concatenate_arrays(*arrays):
    def recursive_concatenate(arrays, result=None):
        if not arrays:
            return result or []
        
        array = arrays[0]
        next_arrays = arrays[1:]
        
        if len(array) < len(next_arrays):
            return recursive_concatenate(next_arrays, [None] * (len(next_arrays) - len(array)) + result)
        else:
            return recursive_concatenate(next_arrays, array + result)
    
    return recursive_concatenate(list(map(list, arrays)))

# Example usage
array1 = [1, 2, 3]
array2 = ['a', 'b']
array3 = [4, 5]

print(concatenate_arrays(array1, array2, array3))
