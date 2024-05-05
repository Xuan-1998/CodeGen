def max_score(score, k, z):
    n = len(score)
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i > k or j < 0 or j >= min(k+1, z+1):
            return 0
        if j == 0:
            return sum(score[:i])
        return max(dp(i-1, j+1) + score[i], dp(i-1, j-1) + score[i-1]) if i > 0 else sum(score[:i])

    return dp(0, 0)

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    score = list(map(int, input().split()))
    print(max_score(score, k, z))
