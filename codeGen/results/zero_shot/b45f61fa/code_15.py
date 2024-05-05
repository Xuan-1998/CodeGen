# Define the function to find the minimum number of multiplications
def min_multiplications(p):
    n = len(p)
    # Initialize a table to store the results of subproblems
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    # Fill the table using dynamic programming
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                q = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]
                if q < dp[i][j]:
                    dp[i][j] = q
    # Find the minimum number of multiplications and construct the parenthesization
    min_mults = dp[0][n-1]
    parenthesization = ''
    i, j = 0, n-1
    while i < j:
        k = i
        for _ in range(i+1, j+1):
            if dp[i][_]*p[_]*dp[_,j] == min_mults:
                k = _
                break
        parenthesization += f'({str(ord('A')+i)}*{str(ord('A')+k))}*{str(ord('A')+j))}'
        i, j = k+1, j-1
    return parenthesization

# Read the input from stdin and print the result to stdout
n = int(input())
p = [int(i) for i in input().split()]
print(min_multiplications(p))
