def can_form_polygon():
    n = int(input())
    moods = list(map(int, input().split()))
    
    dp = {(0, 0): "NO"}
    for i in range(n):
        for k_count in range(i+1):
            mood_sum = sum(moods[:i+1])
            if (k_count-1) % n != 0:
                dp[(mood_sum, k_count)] = "YES" if (mood_sum % n) < n//3 and k_count == n-1 else "NO"
    
    return dp.get((sum(moods), n), "NO")

print(can_form_polygon())
