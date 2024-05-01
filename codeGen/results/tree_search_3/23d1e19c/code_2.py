import sys

def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    path = list(map(int, input().split()))

    dp = [-1] * (n + 1)
    max_recomputations = 0

    for i in range(n):
        if i == 0:
            dp[i] = 0
        else:
            min_recomputations = float('inf')
            for j in range(i - 1, -1, -1):
                if follow_recommendation(path[j]):
                    min_recomputations = min(min_recomputations, dp[path[j]] + 1)
                elif dp[j] != -1:
                    min_recomputations = min(min_recomputations, dp[j] + 1)

            max_recomputations = max(max_recomputations, min_recomputations if i < k else 0)

        print(f"{min_recomputations} {max_recomputations}")
