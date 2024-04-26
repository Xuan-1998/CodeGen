def merge_arrays(*args):
    max_len = max(len(arr) for arr in args)
    result = []
    
    for i in range(max_len):
        for arr in args:
            if i < len(arr):
                result.append(arr[i])
            else:
                result.append(None)
                
    return result

# Example usage
arr1 = [1, 2, 3]
arr2 = ['a', 'b', 'c']
arr3 = [True, False]

print(merge_arrays(*[arr1, arr2, arr3]))
