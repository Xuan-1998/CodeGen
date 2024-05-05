def can_form_polygon(n, moods):
    dp = {(0, 0): "NO"}
    for i, mood in enumerate(moods, start=1):
        k_count = (k_count + 1) if mood == 1 else 0
        mood_sum = mood_sum + mood
        if (n // 2 <= k_count and mood_sum == k_count):
            dp[(k_count, mood_sum)] = "YES"
    return dp.get((k_count, mood_sum), "NO")

n = int(input())
moods = list(map(int, input().split()))
print(can_form_polygon(n, moods))
