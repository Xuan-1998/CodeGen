def matrix_chain_order(p):
    n = len(p)
    dp = [[0] * n for _ in range(n)]
    
    # Initialize base case
    for i in range(n):
        dp[0][i] = 0
    
    # Fill up the dynamic programming table
    for chain_len in range(2, n+1):
        for start_idx in range(n-chain_len+1):
            end_idx = start_idx + chain_len - 1
            dp[start_idx][end_idx] = float('inf')
            for cut_idx in range(start_idx, end_idx):
                cost = dp[start_idx][cut_idx] + dp[cut_idx+1][end_idx] + p[start_idx]*p[cut_idx+1]*p[end_idx]
                if cost < dp[start_idx][end_idx]:
                    dp[start_idx][end_idx] = cost
    
    # Reconstruct the optimal parenthesization order
    min_cost = dp[0][n-1]
    path = []
    current_idx = n-1
    while current_idx > 0:
        for cut_idx in range(current_idx, 0, -1):
            if dp[current_idx][cut_idx] == min_cost - p[current_idx]*p[cut_idx+1]*p[cut_idx]:
                path.append(f"({chr(ord('A')+current_idx)})")
                current_idx = cut_idx
                break
    
    return "".join(reversed(path))
