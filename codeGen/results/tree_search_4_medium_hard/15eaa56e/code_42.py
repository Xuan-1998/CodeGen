import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    
    # Group rows together based on their common columns
    row_groups = defaultdict(list)
    for i, row in enumerate(table):
        key = tuple(sorted(row))
        row_groups[key].append(i)

    # Initialize the maximum column index that needs processing
    max_col = m

    while max_col:
        # Process each group of rows independently
        for row_group in row_groups.values():
            row_table = [table[i] for i in row_group]
            
            # Check if the subtable is sorted in non-decreasing order
            if not is_sorted(row_table):
                print("No")
                return

        # Decrement the maximum column index that needs processing
        max_col -= 1

    print("Yes")

def is_sorted(table):
    for col in range(len(table[0])):
        values = [row[col] for row in table]
        
        # Check if the subtable is sorted in non-decreasing order
        for i in range(1, len(values)):
            if values[i] < values[i-1]:
                return False

    return True

if __name__ == "__main__":
    solve()
