# Read input
n = int(input())
moods = list(map(int, input().split()))

# Check if there are at least 3 knights
if n < 3:
    print("NO")
else:
    # Initialize count of good and bad moods
    good_mood_count = 0
    bad_mood_count = 0

    # Count the number of good and bad moods
    for mood in moods:
        if mood == 1:
            good_mood_count += 1
        else:
            bad_mood_count += 1

    # Check if a regular polygon can be formed
    if (n - 3) % 2 != 0:  # If n is odd, then the number of vertices must also be odd
        print("NO")
    elif good_mood_count <= (n - 3) // 2:
        print("YES")
    else:
        print("NO")
