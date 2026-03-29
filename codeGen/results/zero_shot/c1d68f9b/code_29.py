# Step 1: Read the input
n = int(input())
moods = list(map(int, input().split()))

# Step 2: Count the number of knights with good moods (i.e., their mood is 1)
good_knights = sum(moods)

# Step 3: Check if a regular polygon can be formed
if n % (good_knights + 1) != 0:
    print("NO")
else:
    print("YES")
