def is_sorted_subtable(table):
    n, m = len(table), len(table[0])
    k = len(tasks)
    
    dp_table = [[[0, 0] for _ in range(m)] for _ in range(n) for _ in range(k)]
    
    for i in range(n):
        for j in range(m):
            for task_idx, (l, r) in enumerate(tasks):
                if l <= i < r:
                    # Identify sorting columns
                    prev_val = table[i-1][j] if i > 0 else float('-inf')
                    if table[i][j] != prev_val:
                        first_violation = j
                        break
                    
                    # Update dynamic programming table
                    dp_table[i][j][task_idx] = [table[i][j], 1]
                elif i == r-1:  # Last row for the task
                    if dp_table[i][j][task_idx][0] > prev_val:
                        dp_table[i][j][task_idx] = [dp_table[i][j][task_idx][0], 1]
    
    for task_idx in range(k):
        max_count = 0
        for j in range(m):
            if dp_table[n-1][j][task_idx][1] > max_count:
                max_count = dp_table[n-1][j][task_idx][1]
        if max_count > 0:
            return "Yes"
    return "No"

# Example usage
table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tasks = [(1, 2), (2, 3)]
print(is_sorted_subtable(table))  # Output: Yes

