import sys

def can_form_polygon():
    n, = map(int, input().split())
    moods = list(map(int, input().split()))

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for k_count in range(1, n + 1):
        mood_sum = sum(mood for mood in moods[:k_count])
        if k_count % n == 0 and mood_sum % n == 0:
            dp[k_count][mood_sum] = -1
        else:
            dp[k_count][mood_sum] = 1

    for k_count in range(2, n + 1):
        for mood_sum in range(k_count * n, -1, -1):
            if dp[k_count - 1][mood_sum - (k_count % n)] == 1:
                dp[k_count][mood_sum] = 0
            else:
                dp[k_count][mood_sum] = -1

    result = "YES" if dp[n][sum(moods)] >= 0 else "NO"
    print(result)

can_form_polygon()
