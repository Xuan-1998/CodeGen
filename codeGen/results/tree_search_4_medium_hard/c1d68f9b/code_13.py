from sys import stdin

def can_form_polygon(moods):
    dp = [False] * 2
    dp[0] = True  # initialize with 'invalid'

    for mood in moods:
        dp.append(dp[-1] and mood == 1)  # update the dynamic programming table

    return "YES" if any(dp[i] and i % 3 == 0 for i in range(len(dp) - 2)) else "NO"

n = int(stdin.readline())
moods = list(map(int, stdin.readline().split()))

print(can_form_polygon(moods))
