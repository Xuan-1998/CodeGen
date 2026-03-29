def min_remove Signs, L, R:
    n = len(Signs)
    memo = [[-1] * (R + 1) for _ in range(n + 1)]
    
    def dp(i, j):
        if i > j:
            return 0
        
        if memo[i][j] != -1:
            return memo[i][j]
        
        # base case: only one element
        if i == j:
            return Signs[i] == '+'
        
        # calculate the sum of signs for the left and right halves
        left_sum = dp(i, (i + j) // 2)
        right_sum = dp((i + j) // 2 + 1, j)
        
        # choose the minimum number of elements to remove from either half
        total_sum = left_sum if Signs[i] == '+' else -left_sum
        for k in range(i + 1, j + 1):
            total_sum += (Signs[k] == '+') - (-Signs[k] == '+)
            if total_sum < 0:
                return dp(i, k - 1) + (k - i + 1) + dp(k + 1, j)
        
        # store the result in memo
        memo[i][j] = min(dp(i, (i + j) // 2), dp((i + j) // 2 + 1, j)) + 1
        
        return memo[i][j]
    
    for _ in range(int(input())):
        n, q = map(int, input().split())
        Signs = input()
        queries = [map(int, input().split()) for _ in range(q)]
        
        for L, R in queries:
            print(dp(0, n - 1))
