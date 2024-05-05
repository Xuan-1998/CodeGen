def solve():
    n = int(input())
    moods = list(map(int, input().split()))
    
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    max_good_moods = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if moods[i - 1]:
            max_good_moods[i] = max_good_moods[i - 1] + 1
        else:
            max_good_moods[i] = 0
        
        for j in range(i):
            if max_good_moods[j] and moods[i - 1]:
                dp[j][i] = True
    
    for i in range(n, -1, -1):
        if dp[0][i]:
            return "YES"
    
    return "NO"

print(solve())
