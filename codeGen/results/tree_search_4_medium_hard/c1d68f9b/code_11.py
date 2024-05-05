def can_form_polygon(knights_moods):
    n = len(knights_moods)
    dp = [1]  # Initialize the dynamic programming table
    max_length = 1

    for i in range(1, n):
        if knights_moods[i] == 0:
            dp = [max(dp)]
        else:
            dp = [max(i) + 1 for i in dp]
            if len(dp) > max_length:
                max_length = len(dp)

    return "YES" if max_length >= 3 else "NO"


# Read the input from stdin
n, *knights_moods = map(int, input().split())
print(can_form_polygon(knights_moods))
