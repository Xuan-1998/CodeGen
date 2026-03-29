# Step 1: Read the input
n = int(input())
moods = list(map(int, input().split()))

# Step 2: Check if there are at least 3 knights
if n < 3:
    print("NO")
    exit()

# Step 3: Initialize a variable to track the total number of good moods
good_moods = sum(moods)

# Step 4: If the total number of good moods is equal to the number of knights, 
#         then it's possible to form a regular polygon with all good moods
if good_moods == n:
    print("YES")
else:
    print("NO")
