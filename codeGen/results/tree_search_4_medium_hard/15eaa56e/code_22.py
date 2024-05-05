def is_sorted_subtable(table, l, r):
    n, m = len(table), len(table[0])
    states = [[[False, -float('inf')] for _ in range(m)] for _ in range(n)]
    
    # Initialize the base case (when the subtable consists of only one row)
    for j in range(m):
        max_val = table[0][j]
        is_sorted = True
        for i in range(1, n):
            if table[i][j] <= max_val:
                max_val = table[i][j]
            else:
                is_sorted = False
                break
        states[0][j] = [is_sorted, max_val]

    # Fill the 3D array using dynamic programming
    for i in range(1, n):
        for j in range(m):
            is_sorted = states[i-1][j][0]
            max_val = states[i-1][j][1]
            if table[i][j] <= max_val:
                states[i][j] = [is_sorted, max_val]
            else:
                states[i][j] = [False, -float('inf')]

    # Check if the subtable is sorted in at least one column for each task
    for l, r in tasks:
        for j in range(m):
            is_sorted = states[r][j][0]
            max_val = states[r][j][1]
            if is_sorted and table[l-1][j] <= max_val:
                return "Yes"
    return "No"

# Read input from stdin
n, m, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
tasks = [[int(i) for i in input().split()] for _ in range(k)]

print(is_sorted_subtable(table, tasks))
