n = int(input())
marks_above = list(map(int, input().split()))

highest_level = 0
sum_below = 0

for i in range(n):
    # Calculate the minimum water level for the current day
    current_level = max(highest_level, i + 1 - marks_above[i])
    # Update the sum of marks below the water level
    sum_below += current_level - 1 - marks_above[i]
    # Update the highest water level seen so far
    highest_level = max(highest_level, current_level)

print(sum_below)
