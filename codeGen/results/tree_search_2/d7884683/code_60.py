def partition_count(arr):
    n = len(arr)
    table = [[0, 0] for _ in range(n + 1)]
    
    # Initialize the base case (partition_count = 0) for each subarray
    for i in range(1, n + 1):
        table[i][1] = i - 1
    
    for partition_count in range(1, n // 2 + 1):
        for i in range(partition_count * 2, n + 1):
            table[i][0] = max(table[i - j][0] + (arr[i - 1] == arr[j - 1]), table[i - 1][0])
    
    return table[n][0]
