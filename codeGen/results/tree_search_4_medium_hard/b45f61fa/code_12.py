def min_multiplications(p):
    n = len(p)
    dp = [[0] * (n-1) for _ in range(n-1)]
    
    for i in range(n-1):  # consider all possible split positions
        if i == 0:
            dp[0][i] = p[0]*p[i+1]
        elif i == n-2:
            dp[0][i] = 0  # no need to multiply at the last position
        else:
            min_cost = float('inf')
            for k in range(i):  # try splitting at each possible position
                cost = dp[0][k-1] + p[k]*p[i+1] + dp[k][i]
                if cost < min_cost:
                    min_cost = cost
            dp[0][i] = min_cost
    
    result = ''
    i, j = 0, n-2
    while i < j:  # construct the optimal parenthesization
        min_cost = float('inf')
        for k in range(i, j):  # try splitting at each possible position
            cost = dp[i][k] + p[k+1]*p[j] + dp[k+1][j]
            if cost < min_cost:
                min_cost = cost
                best_split = k+1
        result += '(' + str(best_split) + ')'
        i, j = 0, best_split-1
    
    return result

n = int(input())
p = list(map(int, input().split()))
print(min_multiplications(p))
