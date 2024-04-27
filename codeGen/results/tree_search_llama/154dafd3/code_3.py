def round_to_nearest_multiple(arr):
    result = []
    for num in arr:
        closest_multiple = None
        min_diff = float('inf')
        
        # Iterate over all possible multiples of 5
        for i in range(int(num), int((num + 0.99) / 0.2) * 10, 5):
            diff = abs(num - i)
            
            # Update the closest multiple if a smaller difference is found
            if diff < min_diff:
                min_diff = diff
                closest_multiple = i
            
        result.append(closest_multiple)
    
    return result

# Example usage:
numbers = list(map(float, input().split()))
print(round_to_nearest_multiple(numbers))
