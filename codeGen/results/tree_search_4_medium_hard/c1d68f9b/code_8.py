import sys

def can_form_polygon(moods):
    n = len(moods)
    dp = [False] * (n // 3 + 1)
    dp[0] = True
    
    for i in range(n):
        if i % (n // 3) >= n // 3:
            continue
        mood_sum = sum(mood for mood in moods[:i+1])
        k_count = sum(1 for mood in moods[:i+1] if mood == 1)
        
        if k_count * 2 >= i + 1 and (k_count * 2) % n == 0:
            dp[i // (n // 3)] = True
    
    return 'YES' if any(dp) else 'NO'

# Read input from stdin
n = int(sys.stdin.readline())
moods = [int(mood) for mood in sys.stdin.readline().split()]

print(can_form_polygon(moods))
