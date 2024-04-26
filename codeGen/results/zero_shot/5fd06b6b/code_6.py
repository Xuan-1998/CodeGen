def min_sum_marks_below_water(n, marks_above):
    highest_mark = 0
    sum_below = 0
    
    for i in range(n):
        # Calculate marks below the water level for the current day
        below_today = highest_mark - marks_above[i]
        sum_below += below_today
        
        # Update the highest water level mark if a new mark is added today
        if marks_above[i] == highest_mark:
            highest_mark += 1
    
    return sum_below

# Read input from stdin
n = int(input().strip())
marks_above = list(map(int, input().strip().split()))

# Calculate and print the result
print(min_sum_marks_below_water(n, marks_above))
