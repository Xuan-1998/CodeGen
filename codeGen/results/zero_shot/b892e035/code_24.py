import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    probs = []
    for i in range(n):
        A_i, P_A_i = map(float, sys.stdin.readline().split())
        B_i, P_B_i = map(float, sys.stdin.readline().split())
        # Calculate the probability of ticket i not being numbered with A_i
        P_not_i = 1 - P_A_i
        probs.append(P_not_i)
    # Calculate the probability that all tickets have distinct numbers
    prob_distinct = 1
    for i in range(n):
        prob_distinct *= probs[i]
    # Handle rounding errors
    prob_distinct *= 1e6
    print(int(prob_distinct))
