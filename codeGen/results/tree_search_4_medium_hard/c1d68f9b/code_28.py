from collections import deque

def can_form_polygon():
    n = int(input())
    moods = list(map(int, input().split()))
    
    memo = [[-1]*2 for _ in range(n+1)]
    
    def dfs(k, prev_mood):
        if k > 0 and k % (k+1) != 0:
            return "NO"
        
        if memo[k][prev_mood] != -1:
            return memo[k][prev_mood]
        
        good_moods = sum(moods[:k])
        bad_moods = n - good_moods
        
        if prev_mood == moods[-1]:
            return "YES" if k % 2 == 0 else "NO"
        
        if good_moods >= (k+1):
            memo[k][prev_mood] = "YES"
            for i in range(k-1, -1, -1):
                if moods[i] != prev_mood:
                    break
            memo[k][prev_mood] = "NO" if i == 0 else dfs(i, not prev_mood)
            return memo[k][prev_mood]
        elif bad_moods >= (k+1):
            memo[k][prev_mood] = "YES"
            for i in range(k-1, -1, -1):
                if moods[i] != prev_mood:
                    break
            memo[k][prev_mood] = "NO" if i == 0 else dfs(i, not prev_mood)
            return memo[k][prev_mood]
        else:
            memo[k][prev_mood] = "NO"
            return memo[k][prev_mood]
    
    print(dfs(n, 0))
