# Step 1: Read the input
n = int(input())
moods = list(map(int, input().split()))

# Step 2: Calculate the total count of knights with good mood
good_knights = sum(moods)

# Step 3: Check if a regular polygon can be formed
if n <= 3:
    print("YES" if good_knights == 0 or good_knights == n else "NO")
else:
    print("YES" if good_knights % (n - 2) == 0 and good_knights >= 1 else "NO")

