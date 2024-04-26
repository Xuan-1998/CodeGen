n = int(input())  # Read the number of days
marks_above = list(map(int, input().split()))  # Read the marks above the water level for each day

max_water_level = 0
total_marks_below = 0

for mi in marks_above:
    max_water_level = max(max_water_level, mi + 1)
    total_marks_below += max_water_level - 1 - mi

print(total_marks_below)
