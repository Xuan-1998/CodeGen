def can_cross(stones):
    n = len(stones)
    dp = [False] * (n + 1)

    dp[0] = True

    for i in range(1, n):
        for k in range(3):
            jump = i - k - 1
            if 0 <= jump < i and dp[jump]:
                dp[i] = True
                break

    return dp[-1]

# Test cases
print(can_cross([0, 1, 2, 4, 5])) # Output: True
print(can_cross([0, 2, 3, 6, 8])) # Output: False
