import sys

# Read the input moods
moods = [int(mood) for mood in sys.stdin.readline().split()]

# Initialize variables
n = len(moods)
good_knights = sum(1 for mood in moods if mood == 1)

# Check if a polygon is possible
if n % good_knights == 0 and good_knights >= 3:
    print("YES")
else:
    print("NO")
