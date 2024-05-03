import sys

def correct_numbering_prob(tickets):
    memo = {}
    def dp(i, used):
        if (i, tuple(used)) in memo:
            return memo[(i, tuple(used))]
        if i == 0:
            return 1.0
        prob = 0.0
        for j in range(2):
            if not any(n == j+1 for n in used):
                prob += tickets[i-1][j] * dp(i-1, used + (j+1,))
        memo[(i, tuple(used))] = prob
        return prob
    return sum(dp(i, []) for i in range(tickets[0]))


T = int(input())
for _ in range(T):
    n = int(input())
    tickets = [list(map(float, input().split())) for _ in range(n)]
    print(round(sum(dp(i, []) for i in range(n)) if n else 1.0, 6))
