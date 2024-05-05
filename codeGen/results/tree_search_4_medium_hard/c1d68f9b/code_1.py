def polygon_possible():
    n = int(input())
    moods = list(map(int, input().split()))
    
    dp = {(0, 0): "NO"}
    for i, mood in enumerate(moods):
        for (k_count, mood_sum) in list(dp.keys()):
            if k_count == i // 2 and mood_sum % 2 == 0:
                return "YES"
            dp[(k_count + int(mood), mood_sum + mood)] = "NO"
    
    print("NO")

polygon_possible()
