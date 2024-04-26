n = int(input())
marks_above = list(map(int, input().split()))

# Initialize the sum of marks below the water level to 0.
sum_below = 0
# Initialize the current highest possible water level to 0.
current_highest_level = 0

for i in range(n):
    # The water level for the current day is at most one level lower than the previous day's level.
    current_highest_level = max(current_highest_level - 1, marks_above[i])
    # Calculate the number of marks below the water level for the current day.
    marks_below = i - current_highest_level
    # Update the sum of marks below the water level.
    sum_below += marks_below

print(sum_below)
