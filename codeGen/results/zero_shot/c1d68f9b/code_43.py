# Read input
n = int(input())
moods = list(map(int, input().split()))

# Initialize variable to store the result
can_form_polygon = True

# Iterate over each knight
for i in range(n):
    # Check if the current knight is not in a good mood (0)
    if moods[i] == 0:
        # If any knight is not in a good mood, we cannot form a polygon
        can_form_polygon = False
        break

# Print the result
print("YES" if can_form_polygon else "NO")
