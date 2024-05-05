from collections import defaultdict

def min_changes():
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        s = input()
        
        # Initialize a dictionary to store the results of subproblems
        dp = defaultdict(lambda: [float('inf')] * 3)
        dp[0][0] = 0
        
        # Calculate the minimum number of changes needed for each substring
        for i in range(n):
            if i >= k:
                prev = s[i-k+1:i+1]
            else:
                prev = 'R' + ('RGB'[s[:i].index(s[i]) % 3] * (k-1))
            
            for j in range(3):
                c = 'RGB'[j]
                if c == prev[j%k]:
                    dp[i][j] = dp[i-1][j] if i > 0 else 0
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j % 3])
            
        print(min(dp[-1]))

min_changes()
