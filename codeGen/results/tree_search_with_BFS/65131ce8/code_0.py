python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    if sum(d) != N - 1:
        print(0)
        return
    
    # dp[i][j] will store the number of ways to form a subtree with i nodes and j good vertices
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case
    dp[1][1] = 1
    
    # Iterate over number of nodes from 2 to N
    for nodes in range(2, N + 1):
        for good_vertices in range(1, nodes + 1):
            for left_size in range(1, nodes):
                right_size = nodes - left_size - 1
                if right_size < 0:
                    continue
                for left_good in range(1, good_vertices + 1):
                    right_good = good_vertices - left_good
                    if right_good < 0:
                        continue
                    dp[nodes][good_vertices] += (dp[left_size][left_good] * dp[right_size][right_good]) % MOD
                    dp[nodes][good_vertices] %= MOD
    
    # Calculate the answer
    answer = 0
    for i in range(1, N + 1):
        answer = (answer + dp[N][i]) % MOD
    
    print(answer)


