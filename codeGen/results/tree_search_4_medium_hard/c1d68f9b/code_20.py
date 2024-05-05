def can_form_polygon(moods):
    n = len(moods)
    
    # Initialize dp array with False values for i < 3
    dp = [False] * (n + 1)
    
    # Initialize first three elements of dp array based on moods
    dp[0] = (moods[0] == 1)
    if n >= 2:
        dp[1] = (moods[1] == 1) and (moods[0] != moods[1])
    if n >= 3:
        dp[2] = ((moods[2] == 1) and (moods[1] != moods[2])) or ((moods[2] != 1) and (dp[1]))
    
    # Calculate dp[i] for i > 0
    for i in range(3, n):
        if i % 2 == 0:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1] or ((moods[i] == 1) and (dp[i - 2]))
    
    # Return the answer
    return "YES" if dp[-1] else "NO"
