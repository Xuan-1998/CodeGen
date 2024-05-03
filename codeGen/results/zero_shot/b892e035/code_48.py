import math

T = int(input())  # Number of test cases
for _ in range(T):
    n = int(input())  # Number of tickets
    prob_A = []
    prob_B = []
    for i in range(n):
        P_ai, A_i, B_i = map(float, input().split())
        prob_A.append(P_ai)
        prob_B.append(1 - P_ai)  # Calculate the probability of not choosing A_i
    total_prob = 1
    for p_A, p_B in zip(prob_A, prob_B):
        total_prob *= (p_A * p_B + (1 - p_A) * (1 - p_B))
    print(round(total_prob, 6))  # Round the result to 6 decimal places
