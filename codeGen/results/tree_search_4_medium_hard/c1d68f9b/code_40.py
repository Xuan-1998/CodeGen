def can_form_polygon():
    n = int(input())
    moods = list(map(int, input().split()))
    
    memo = {}
    
    def dp(k, s):
        if (k, s) in memo:
            return memo[(k, s)]
        
        if k == 1:
            return 'YES' if sum(moods[:s]) % n == 0 else 'NO'
        
        result = 'NO'
        for i in range(s, -1, -1):
            if moods[i] == 1 and dp(k-1, i) == 'YES':
                result = 'YES'
                break
        memo[(k, s)] = result
        return result
    
    print(dp(n, len(moods)))
