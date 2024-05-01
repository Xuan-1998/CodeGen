def solve():
    n = int(input())
    s = input()
    dp = [[[] for _ in range(2**n)] for _ in range(n+1)]
    
    # Initialize the base case: the only winning team in the first round is itself.
    for i in range(2**n):
        dp[0][i] = [i]
    
    # Iterate over each round, and update the dp table accordingly.
    for i in range(1, n+1):
        for j in range(2**n):
            if all(int(s[i-k-1]) == int('1' if k < n-i else s[k]) for k in range(i)):
                dp[i][j] = [(k,) for k in range(2**n) if bin(j)[2:].zfill(n-i).count('1') == 1]
    
    # Now, iterate over each round again, and find the winning teams.
    for i in range(n, -1, -1):
        for j in range(2**i-1):
            if dp[i][j]:
                for team in dp[i][j]:
                    print(team)
