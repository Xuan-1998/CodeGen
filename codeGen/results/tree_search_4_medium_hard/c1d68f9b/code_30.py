import sys

def can_form_polygon():
    n = int(input())
    moods = list(map(int, input().split()))

    dp = [[False] * 2 for _ in range(n + 1)]

    for i in range(3):
        dp[i][moods[i]] = True

    for k in range(3, n + 1):
        for prev_mood in range(2):
            good_moods = sum(m == 1 for m in moods[k-3:k])
            if (prev_mood == 0 and good_moods % 2 == 0) or (prev_mood == 1 and good_moods % 2 != 0):
                dp[k][moods[k-1]] = True

    return "YES" if dp[n][1] else "NO"

print(can_form_polygon())
