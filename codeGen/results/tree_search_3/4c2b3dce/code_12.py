def solution():
    s = input().strip()
    lcp = min("AB", "BA")  # find the longest common prefix between "AB" and "BA"
    
    dp = [[0, 0] for _ in range(len(lcp) + 1)]
    
    for i in range(1, len(s)):
        if s[i] == lcp[0]:
            dp[0][0] = 1
        elif s[i] == lcp[1]:
            dp[0][1] = 1
        else:
            dp[0][0] = 0
            dp[0][1] = 0
        
        for j in range(len(lcp)):
            if s[i] == lcp[j]:
                dp[j + 1][0] = (dp[j][0] or s[i] == 'A')
                dp[j + 1][1] = (dp[j][1] or s[i] == 'B')
    
    for i in range(len(lcp) - 1, -1, -1):
        if dp[i][0] and dp[i][1]:
            print("YES")
            return
    print("NO")

solution()
