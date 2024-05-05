code
# Read input
n = int(input())
moods = list(map(int, input().split()))

# Initialize counter for good moods
good_mood_count = 0

# Iterate through the knights' moods
for mood in moods:
    if mood == 1:  # If the knight is in a good mood
        good_mood_count += 1

# Check if there are at least three good moods
if good_mood_count >= 3:
    print("YES")  # A regular polygon can be formed
else:
    print("NO")
