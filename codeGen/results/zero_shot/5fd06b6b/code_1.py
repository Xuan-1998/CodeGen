def find_minimum_marks_below_water(n, marks_above_water):
    total_marks_below_water = 0
    for i in range(n):
        marks_below_water = i - marks_above_water[i] - 1
        total_marks_below_water += marks_below_water
    return total_marks_below_water

# Read input
n = int(input().strip())
marks_above_water = list(map(int, input().strip().split()))

# Calculate and print the result
print(find_minimum_marks_below_water(n, marks_above_water))
