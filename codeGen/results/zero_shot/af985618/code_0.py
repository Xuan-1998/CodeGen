MOD = 998244353

def add(x, y):
    return (x + y) % MOD

def main():
    n = int(input())
    elements = [input().split() for _ in range(n)]
    
    # dp[i] will store the sum of all f(B) where B includes the first i elements of A
    dp = [0] * (n + 1)
    dp[0] = 1  # There is one subsequence of length 0, the empty subsequence
    
    # prefix_sums[i] will store the sum of elements in all sets considered up to the i-th element
    prefix_sums = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if elements[i-1][0] == '+':
            x = int(elements[i-1][1])
            for j in range(i, 0, -1):
                dp[j] = add(dp[j], dp[j-1])  # Include x in the subsequence
                prefix_sums[j] = add(prefix_sums[j], (dp[j-1] * x) % MOD)
            dp[0] = add(dp[0], dp[0])  # Empty subsequence case
        else:
            for j in range(i):
                prefix_sums[j] = add(prefix_sums[j], prefix_sums[j])
    
    result = sum(prefix_sums) % MOD
    print(result)

if __name__ == "__main__":
    main()
