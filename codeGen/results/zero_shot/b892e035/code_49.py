import sys

def calculate_probability(n, A, B):
    # Calculate the total probability of all tickets having distinct numbers
    total_prob = 1.0
    for i in range(n):
        # Calculate the probability of the current ticket having distinct numbers
        prob = P_i * (1 - P_i) / 2.0
        total_prob *= prob

    return round(total_prob, 6)

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    A = [int(x) for x in sys.stdin.readline().split()]
    B = [int(x) for x in sys.stdin.readline().split()]
    P = [float(x) for x in sys.stdin.readline().split()]

    probability = calculate_probability(n, A, B)
    print(probability)

