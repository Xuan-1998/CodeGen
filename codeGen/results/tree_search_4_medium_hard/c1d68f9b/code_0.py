def can_form_polygon(moods):
    n = len(moods)
    total_knights = n

    # Initialize dynamic programming table
    dp = [[[False for _ in range(total_knights + 1)] for _ in range((total_knights // 2) + 1)] for _ in range(n + 1)]

    # Base case: 0 knights can't form a polygon
    for j in range(total_knights + 1):
        dp[0][j][0] = False

    # Iterate through each knight
    for i in range(1, n + 1):
        good_knights = sum(1 for mood in moods[:i] if mood == 1)
        good_mood_sum = sum(mood for mood in moods[:i] if mood == 1)

        # Update dynamic programming table
        for j in range((total_knights // 2) + 1):
            if good_knights <= j and good_mood_sum <= j:
                dp[i][j][0] = True
                break

    return "YES" if dp[n-1][total_knights//2][0] else "NO"

# Example usage:
moods = [int(input()) for _ in range(int(input()))]
print(can_form_polygon(moods))
