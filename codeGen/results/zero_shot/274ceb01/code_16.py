n = int(input())  # Read the number of days from stdin
marks_above = list(map(int, input().split()))  # Read the number of marks strictly above the water on each day

# Sort the days based on the number of marks above the water
sorted_days = sorted((m, i) for i, m in enumerate(marks_above))

total_marks_below = 0
for _, i in sorted_days:
    total_marks_below += sum(range(i))  # Calculate the sum of marks below the water level for each day

print(total_marks_below)  # Print the minimum possible sum of marks below the water level
