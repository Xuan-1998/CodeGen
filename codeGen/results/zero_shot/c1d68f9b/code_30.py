# Step 1: Read input
n = int(input())
moods = list(map(int, input().split()))

# Step 2: Check if there are at least 3 knights
if n < 3:
    print("NO")
else:
    # Step 3: Count the number of good moods (1) and bad moods (0)
    good_moods = sum(moods)

    # Step 4: If all knights are in a good mood, it's always possible to form a polygon
    if good_moods == n:
        print("YES")
    # Step 5: If exactly half of the knights are in a good mood, it's also possible to form a polygon
    elif good_moods == n // 2:
        print("YES")
    else:
        print("NO")
