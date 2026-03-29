def solve():
    n = int(input())
    s = input().strip()
    a = list(map(int, input().split()))
    
    # Initialize dp table with dimensions (n+1) x 27
    dp = [[0] * 27 for _ in range(n + 1)]
    
    # Initialize first row of the dp table
    for i in range(26):
        if s.count(chr(i+97)) == 1:
            dp[0][i] = 1
    
    # Fill up the rest of the dp table using bottom-up approach
    for i in range(1, n + 1):
        for k in range(min(k+1, 27)):
            if k > i // a[k-1]:
                dp[i][k] = 0
            else:
                m = 0
                for j in range(i):
                    if s[j] != chr((j // (a[ord(s[j])-97]) + 96)):
                        m += 1
                dp[i][k] = (m // (i+1)) + 1
    
    # Find the number of ways to split the message into k substrings with unique characters
    ways_to_split = sum(dp[n-1][j] for j in range(1, min(k+1, 27)))
    
    # Find the length of the longest substring over all possible splits
    max_length = max(dp[n-1][j] for j in range(1, min(k+1, 27)))
    
    # Find the minimum number of substrings over all possible splits
    min_substrs = min(j for j in range(1, min(k+1, 27)) if dp[n-1][j])
    
    print(ways_to_split % (10**9 + 7))
    print(max_length)
    print(min_substrs)

if __name__ == "__main__":
    solve()
