from collections import defaultdict

def distinctSums(A):
    n = len(A)
    max_sum = sum(A)
    
    dp = [[set() for _ in range(max_sum + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(max_sum + 1):
            if A[i - 1] > j:
                dp[i][j] = set(dp[i - 1][j])
            else:
                if j >= A[i - 1]:
                    subset_sums = {k for k in dp[i - 1][j - A[i - 1]]}
                    subset_sums.add(j)
                    dp[i][j] = subset_sums
                else:
                    dp[i][j] = set(dp[i - 1][j])
    
    result = []
    for j in range(max_sum + 1):
        if dp[n][j]:
            result.append(str(j))
    
    return ' '.join(sorted(result))

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    print(distinctSums(A))
