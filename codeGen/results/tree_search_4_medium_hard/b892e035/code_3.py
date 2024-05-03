from collections import defaultdict

# Read input and initialize variables
T = int(input())
dp_table = defaultdict(lambda: [0, 0])

for _ in range(T):
    n = int(input())
    P_A = []
    A_B = []

    for i in range(n):
        p, a, b = map(int, input().split())
        P_A.append(p)
        A_B.append((a, b))

    # Initialize the DP table
    dp_table[0] = [0, 1]

    for i in range(n):
        used = set()
        for j in range(2):  # probability and number
            if j == 0:
                new_used = {j} | used
            else:
                new_used = used.copy()
            p, a, b = A_B[i]
            if (new_used | {a, b}) not in [k for k, v in dp_table.items()]:
                dp_table[(i + 1) | new_used] = [(i, j), P_A[i] / sum(P_A)]
            else:
                dp_table[(i + 1) | new_used][1] += P_A[i] / sum(P_A)
        if (n, used) in [k for k, v in dp_table.items()]:
            print(dp_table[n][1])
        break
