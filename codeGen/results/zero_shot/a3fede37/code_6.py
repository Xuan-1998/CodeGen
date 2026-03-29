def max_path_sum(arr):
    def max_gain(i):
        # Initialize maximum gain
        left_gain = right_gain = 0
        
        # Check if left child exists
        if i*2 + 1 < len(arr):
            left_gain = arr[i*2 + 1]
        if i*2 + 2 < len(arr) and arr[i*2 + 1] > arr[i]:
            right_gain = arr[i*2 + 2]
        
        # Update maximum gain
        max_val = arr[i] + max(left_gain, right_gain)
        
        return max_val

    if len(arr) == 0:
        return 0
    
    return max(max_path_sum([arr[i]] for i in range(len(arr)) if arr[i] > arr[0]), max_gain(0))

# Test the function
root = [4,2,7,1,3,6,5]
print(max_path_sum(root))
