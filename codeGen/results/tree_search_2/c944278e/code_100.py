def solve(n):
    # Initialize the dp table with all possible phases and strings
    dp = [[[[] for _ in range(2)] for _ in range(2**n)] for _ in range(n+1)]

    # Base case: only one winning team when the phase reaches its maximum value (2^N - 1)
    for i in range(2**n):
        dp[n][format(i, 'b').zfill(n)][0] = [i]
        dp[n][format(i, 'b').zfill(n)][1] = [i]

    # Fill up the dp table using a bottom-up approach
    for i in reversed(range(n)):
        for s in range(2**n):
            if format(s, 'b').zfill(n)[i] == '0':
                dp[i][s] = dp[i+1][s << 1]
            else:
                dp[i][s] = [j for j in dp[i+1][s << 1][1] if s >> i & 1 and not any(k > l for k, l in zip(format(j, 'b').zfill(n), format(s, 'b').zfill(n)))]

    # Return the winning teams in ascending order
    return sorted([j for s in range(2**n) for i in range(n+1) if dp[i][s] for j in dp[i][s][0]])

if __name__ == '__main__':
    n = int(input())
    print(*solve(n), sep='\n')
