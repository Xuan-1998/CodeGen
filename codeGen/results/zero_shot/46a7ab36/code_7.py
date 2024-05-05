python
def count_words(n, m):
    MOD = 10**8 + 7
    
    # Base case: For the first letter, there are n possibilities.
    dp = [[1 for _ in range(m+1)] for _ in range(n)]
    
    for i in range(2, n+1):
        for j in range(m+1):
            if j == 0:
                continue
            # If the index of the letter is i, then it can be placed at any position in the word.
            dp[i-1][j] += sum(dp[k][j-1] for k in range(i) if 2*k > n)
            
    total_words = sum(dp[-1][i] for i in range(m+1))
    
    return total_words % MOD

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(count_words(n, m))
