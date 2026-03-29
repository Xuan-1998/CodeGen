from functools import lru_cache

def max_similarity_score(A, B):
    @lru_cache(None)
    def dp(i, j):
        if i == 0 or j == 0:
            return 0
        if A[i-1] == B[j-1]:
            return dp(i-1, j-1) + (min(i-1, j-1) == 0) * 4
        else:
            return max(dp(i-1, j), dp(i, j-1))

    return max([dp(i, j) for i in range(len(A)+1) for j in range(len(B)+1)])

# Read input from stdin
A = input().strip()
B = input().strip()

print(max_similarity_score(A, B))
