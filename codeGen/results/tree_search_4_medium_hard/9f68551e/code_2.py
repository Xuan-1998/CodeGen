def min_mana_required(input_file):
    with open(input_file, 'r') as f:
        n = int(f.readline())
        monsters = []
        for _ in range(n):
            k, h = map(int, f.readline().split())
            monsters.append((k, h))

    # Initialize DP table
    dp = [[float('inf')] * (max(k) + 1) for _ in range(n + 1)]

    # Base case: no more monsters to cast spells on
    dp[0][0] = 0

    for i in range(1, n + 1):
        k_i, h_i = monsters[i - 1]
        for t in range(max(k) + 1):
            if t < k_i:
                dp[i][t] = min(dp[i-1][max(0, t-k_i+1)] + h_i, dp[i-1][t])
            else:
                dp[i][t] = dp[i-1][t]

    return dp[n][max(k)]
