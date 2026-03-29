def matrix_chain_order(p):
    n = len(p) - 1
    
    # Initialize dp and s arrays with zeros
    dp = [[0 for _ in range(n+1)] for _ in range(n)]
    s = [[0 for _ in range(n+1)] for _ in range(n)]

    # Fill the dp array using bottom-up dynamic programming
    for chain_length in range(2, n+1):
        for i in range(n-chain_length+1):
            j = i + chain_length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                q = p[i] * p[k+1] * dp[i][k] + p[k+1] * p[j+1] * dp[k+1][j]
                if q < dp[i][j]:
                    dp[i][j] = q
                    s[i][j] = k

    # Construct the optimal parenthesization of the matrix chain
    def construct_order(i, j):
        if i == j:
            return 'A' + str(i)
        else:
            k = s[i][j]
            return '(' + construct_order(i, k) + ')' + 'x' + str(p[k]) + '*' + construct_order(k+1, j)

    # Print the optimal parenthesization of the matrix chain
    print(construct_order(0, n-2))

# Read input from stdin and call the function
n = int(input())
p = list(map(int, input().split()))
matrix_chain_order(p)
