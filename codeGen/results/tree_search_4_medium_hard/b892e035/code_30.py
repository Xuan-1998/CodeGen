import sys

def probability(n):
    dp = {(): 1}
    for _ in range(n):
        new_dp = {}
        for prev_state, p in dp.items():
            for i in range(2):
                num = input().strip()
                if int(num) not in prev_state:
                    new_dp[tuple(sorted(list(prev_state) + [int(num)]))] = p * (1 - float(input().strip()) / 100)
        dp = new_dp
    return sum(p for state, p in dp.items())

T = int(input())
for _ in range(T):
    n = int(input())
    print("{:.6f}".format(probability(n)))
