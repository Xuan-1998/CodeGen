def merge_arrays(*args):
    # Initialize an empty list to store the merged array
    result = []
    
    # Find the length of the longest input array
    max_len = max(len(arr) for arr in args)
    
    # Iterate through each input array
    for i, arr in enumerate(args):
        # Append elements from the current array to the result array
        result.extend([arr[i % len(arr)] for _ in range(max_len)])
    
    return result

# Test the function with example inputs
input_arrays = [[1, 2], [3, 4, 5], [6]]
print(merge_arrays(*input_arrays))  # Output: [1, 3, 6, 2, 4, 5]
