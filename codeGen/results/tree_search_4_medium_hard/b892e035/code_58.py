import sys
from collections import defaultdict

def correct_numbering(n, probs):
    memo = defaultdict(float)
    memo[(n, set())] = 1.0

    def dfs(i, seen):
        if i == 0:
            return 1.0 if len(seen) == n else 0.0
        key = (i, frozenset(seen))
        if key in memo:
            return memo[key]
        prob_a, a, b = probs[i-1]
        seen.add(a)
        seen.add(b)
        p = prob_a * dfs(i-1, seen) + (1-prob_a) * dfs(i-1, seen)
        memo[key] = p
        return p

    result = 0.0
    for _ in range(int(input())):
        n = int(input())
        probs = [list(map(float, input().split())) for _ in range(n)]
        result += dfs(n, set())
    print("%.6f" % result)
