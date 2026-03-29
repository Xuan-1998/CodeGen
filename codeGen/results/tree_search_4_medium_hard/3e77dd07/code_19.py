def isScramble(s1, s2):
    if len(s1) != len(s2):
        return False
    
    dp = [[[False] * (len(s2) + 1) for _ in range(len(s1) + 1)] for _ in range(2)]
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[0][i][j] = True
            else:
                for k in range(i):
                    if (s1[k] == s2[j - 1] and dp[1][k][j - 1]) or (s1[i - 1] == s2[k] and dp[1][i - 1][k]):
                        dp[0][i][j] = True
                        break
    
    return dp[0][-1][-1]

# Test the function
while True:
    try:
        s1, s2 = input().split()
        print(int(isScramble(s1, s2)))
    except EOFError:
        break
