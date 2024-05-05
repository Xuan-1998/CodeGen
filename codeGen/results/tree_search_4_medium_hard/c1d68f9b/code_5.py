from collections import deque

def can_form_polygon():
    n = int(input())
    moods = [int(x) for x in input().split()]

    dp = [(0, 0)]  # Initialize with base case (0 good moods, 0 sum)
    for mood in moods:
        new_dp = []
        for prev_sum, prev_k_count in dp:
            if (prev_sum + mood) % 2 == 0 and prev_k_count >= 3:  # Check validity
                new_dp.append((mood, prev_k_count + int(mood)))
            else:
                new_dp.append((prev_sum, prev_k_count))
        dp = new_dp

    return "YES" if any(x[1] >= 3 for x in dp) else "NO"
