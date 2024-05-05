{
    n, k = map(int, input().split())
    s = input()
    
    dp = [""] * (k + 1)
    for i in range(1, k + 1):
        if i == 1:
            dp[i] = s[0]
        else:
            if i <= len(s):
                delete = dp[i - 1] + s[i - 1]
                duplicate = dp[i - 1] + s[i - 1]
            else:
                delete = ""
                duplicate = dp[i - 1]
            
            dp[i] = min(delete, duplicate)
    
    print(dp[k])
}
