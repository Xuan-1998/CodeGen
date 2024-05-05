import sys

n = int(sys.stdin.readline())
marks_above = list(map(int, sys.stdin.readline().split()))

# Sort days by marks above the water level
sorted_days = sorted((m, i) for i, m in enumerate(marks_above))

# Calculate sum of marks below the water level for each day
sum_marks_below = 0
for _, marks in sorted_days:
    sum_marks_below += marks

print(sum_marks_below)
