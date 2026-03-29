def can_form_polygon():
    n = int(input())
    moods = list(map(int, input().split()))
    
    memo = {}
    def dp(mood_sum, k_count):
        if (mood_sum, k_count) in memo:
            return memo[(mood_sum, k_count)]
        
        if mood_sum == 0 and k_count >= n // 2 + 1:
            return True
        elif mood_sum != 0 and k_count < n // 2:
            return False
        
        result = any(dp((mood_sum - (k_ mood), k_count - 1) for k_, mood in enumerate(moods) if k_ <= i))
        memo[(mood_sum, k_count)] = result
        return result
    
    print("YES" if dp(0, 0) else "NO")

can_form_polygon()
