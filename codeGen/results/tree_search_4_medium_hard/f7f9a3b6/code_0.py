def solve():
    n = int(input())
    s = input()
    a = list(map(int, input().split()))
    
    dp = [[[0] * 27 for _ in range(26)] for _ in range(n+1)]
    dp[0][0][1] = 1
    
    prev_char = -1
    num_unique = 0
    
    for i in range(1, n+1):
        c = ord(s[i-1]) - ord('a')
        
        if s[i-1] == s[i-2]:
            dp[i][c][num_unique] = dp[i-a[c]][c][num_unique]
        else:
            dp[i][c][num_unique+1] = (dp[i-1][prev_char][num_unique] + 
                                         dp[i-1][c][num_unique+1]) % 10**9 + 7
        
        prev_char = c
        num_unique += (s[i-1] != s[i-2])
    
    ways = sum(dp[n][-1][i] for i in range(26))
    longest_substring = max(i for i, c in enumerate(s) if dp[i][c][num_unique+1] > 0)
    min_substrings = min(i for i, c in enumerate(s) if dp[i][c][num_unique] > 0)
    
    print(ways % (10**9 + 7))
    print(longest_substring)
    print(min_substrings)

solve()
