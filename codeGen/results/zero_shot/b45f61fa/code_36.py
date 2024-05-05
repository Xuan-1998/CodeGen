def minMultiplications(p):
    n = len(p)
    
    # Create a table to store the minimum number of multiplications for each subproblem
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    # Fill the table in bottom-up manner
    for chain_length in range(2, n+1):
        for i in range(n-chain_length+1):
            j = i + chain_length - 1
            
            # Calculate the minimum number of multiplications for the current subproblem
            dp[i][j] = float('inf')
            for k in range(i, j):
                q = p[i-1] * p[k] * p[j]
                m = dp[i][k] + dp[k+1][j] + 1
                if m < dp[i][j]:
                    dp[i][j] = m
            
    # Reconstruct the optimal parenthesization from the table
    result = []
    i, j = 0, n-1
    while j > i:
        for k in range(i, j):
            if dp[i][k] + dp[k+1][j] < dp[i][j]:
                result.append('(')
                result.append(chr(65+k))
                result.append(')')
                j = k
                break
        i += 1
    
    # Add the remaining matrix to the end of the string
    result.append(p[i-1])
    
    return ''.join(result)

# Read input from standard input
n = int(input())
p = list(map(int, input().split()))

print(minMultiplications(p))
