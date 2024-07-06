python
MOD = 998244353

def count_good_trees(N, d):
    # dp[i][j] will represent the number of ways to form a tree with i nodes and j good vertices
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case
    dp[1][1] = 1
    
    # Fill the dp table
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(1, i):
                if k > 0 and i - k > 0:
                    dp[i][j] = (dp[i][j] + dp[k][j - 1] * dp[i - k][j]) % MOD
    
    # Calculate the number of good vertices
    good_vertices_count = 0
    for i in range(1, N + 1):
        good_vertices_count = (good_vertices_count + dp[N][i]) % MOD
    
    return good_vertices_count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    result = count_good_trees(N, d)
    print(result)

if __name__ == "__main__":
    main()

