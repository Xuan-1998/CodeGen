def min_sum_marks_below_water(n, marks_above):
    # Calculate the sum of the first n natural numbers
    sum_day_numbers = n * (n + 1) // 2
    # Calculate the sum of marks above the water level
    sum_marks_above = sum(marks_above)
    # Calculate the sum of marks below the water level
    sum_marks_below = sum_day_numbers - sum_marks_above - n
    return sum_marks_below

# Read input from stdin
n = int(input())
marks_above = list(map(int, input().split()))

# Calculate and print the result
print(min_sum_marks_below_water(n, marks_above))
