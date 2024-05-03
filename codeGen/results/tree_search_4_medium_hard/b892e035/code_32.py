import math

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        probabilities = [list(map(float, input().split())) for _ in range(n)]
        dp = {(0,): 1}
        for p, a, b in probabilities:
            new_dp = {}
            for state, prob in list(dp.items()):
                if (a, b) not in state:
                    new_dp[state + ((a, p),)] = prob * p
                    new_dp[state + ((b, 1-p),)] = prob * (1-p)
            dp = new_dp
        print(sum(prob for state, prob in dp.values()))

solve()
