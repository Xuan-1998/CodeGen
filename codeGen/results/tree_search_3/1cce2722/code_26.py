def max_points_earned(sequence):
    n = len(sequence)
    
    # Create a table to store the maximum number of points that can be earned by deleting elements from subsequences.
    dp_table = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        dp_table[i][i] = 1
    
    for length in range(2, n + 1):
        for start_index in range(n - length + 1):
            end_index = start_index + length - 1
            if sequence[end_index] == sequence[start_index]:
                # If the last element is equal to the first element, consider two options:
                # 1. Delete the current element and all elements equal to it.
                # 2. Don't delete the current element.
                dp_table[end_index][end_index] = max(dp_table[start_index + 1][start_index + length - 1], dp_table[start_index][start_index + length - 1])
            else:
                # If the last element is not equal to the first element, consider three options:
                # 1. Delete the current element.
                # 2. Don't delete the current element.
                # 3. Consider deleting elements in both directions from the current element and check if that gives more points.
                dp_table[end_index][end_index] = max(dp_table[start_index + 1][start_index + length - 1], 
                                                     dp_table[start_index][start_index + length - 1], 
                                                     dp_table[start_index + 1][end_index])
    
    return dp_table[n-1][n-1]
