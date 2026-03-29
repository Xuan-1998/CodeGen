import sys

n = int(sys.stdin.readline())
moods = list(map(int, sys.stdin.readline().split()))

good_mood_count = 0
bad_mood_count = 0

for mood in moods:
    if mood == 1:
        good_mood_count += 1
    else:
        bad_mood_count += 1

if abs(good_mood_count - bad_mood_count) <= 1:  # Check the condition
    print("YES")
else:
    print("NO")
