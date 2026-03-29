import sys

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
k = int(sys.stdin.readline())

for task in range(k):
    l, r = map(int, sys.stdin.readline().split())
    
    # Initialize suffix array and maximum value
    suffix_array = []
    max_val = float('-inf')
    
    # Iterate over rows in reverse order
    for row in table[l-1:r]:
        # Find column values for the current column
        col_values = [val for val in row]
        
        # If this is a new combination of values, add it to the suffix array and update max_val
        if len(suffix_array) == 0 or tuple(col_values) != suffix_array[-1]:
            suffix_array.append(tuple(col_values))
            max_val = max(max_val, max(col_values))
        
        # Check if the suffix array is sorted
        if not all(b >= a for a, b in zip(suffix_array, suffix_array[1:])):
            print("No")
            sys.exit()
    
    print("Yes" if len(suffix_array) > 0 else "No")
