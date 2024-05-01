===BEGIN CODE===
def generate_sums(a):
    n = len(a)
    dp = [[set()] for _ in range(n + 1)]
    
    # Base case: Empty set has sum 0
    dp[0][0].add(0)

    for i in range(1, n + 1):
        for j in range(i + 1):
            if j == 0:
                subset_sum = 0
            else:
                subset_sum = a[j - 1] + dp[i - 1][j - 1]
            
            # Add the new sum to the existing sets of sums
            dp[i].append(dp[i - 1][j] | {subset_sum})
    
    return sorted({sum(s) for s in dp[n]})


# Read input from stdin and print output to stdout
n = int(input())
a = [int(x) for x in input().split()]
print(*generate_sums(a), sep=' ')
===END CODE===
