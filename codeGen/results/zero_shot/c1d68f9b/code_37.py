code
# Initialize an empty list to store the moods of knights
moods = []

# Read the number of knights (n) from stdin
n = int(input())

# Read the moods of knights from stdin and append them to the list
for _ in range(n):
    mood = int(input())
    moods.append(mood)

# Check if a regular polygon can be formed with knights in good mood sitting at its vertices
can_form_polygon = True

for i, mood in enumerate(moods):
    # A knight is in a good mood if the number of knights on his left who are also in a good mood is equal to the number of knights on his right who are also in a good mood
    if (mood == 1 and sum(moods[i-1:i]) % 2 != 0) or (mood == 0 and sum(moods[i-1:i]) % 2 == 0):
        can_form_polygon = False
        break

# Print the result to stdout
print("YES" if can_form_polygon else "NO")
code
