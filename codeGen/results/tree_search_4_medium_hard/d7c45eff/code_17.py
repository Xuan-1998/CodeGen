def smallest_string():
    n, k = map(int, input().split())
    s = input()
    
    if k > n:
        return s * (k // len(s)) + s[:k % len(s)]
        
    dp = [[s[:i]] for i in range(k+1)]
    
    for i in range(1, k+1):
        for j in range(i):
            if s[j] < s[i]:
                dp[i].append(dp[j][0])
            elif s[j] > s[i]:
                dp[i].append(s[:j]+s[i:])
                
    return min(dp[k], key=min)

print(smallest_string())
