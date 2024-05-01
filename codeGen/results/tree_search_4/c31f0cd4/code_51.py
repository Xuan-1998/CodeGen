def distinct_sums(N, numbers):
    if N == 0:
        return []
    
    dp = [[set()] for _ in range(N+1)]
    
    for i in range(1, N+1):
        for j in range(max(dp[i-1][0]), sum(numbers)+1):
            new_set = set()
            for k in numbers[:i]:
                if j-k not in dp[i-1][j-k]:
                    new_set.add(j)
            dp[i].append(new_set)
    
    sums = [sum for subset in dp[N] for sum in subset]
    return ' '.join(map(str, sorted(set(sums))))
