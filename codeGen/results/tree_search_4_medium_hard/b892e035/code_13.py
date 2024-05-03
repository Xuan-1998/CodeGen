import sys
from collections import defaultdict

def correct_numbering(n):
    # Initialize a table with dimensions (n+1, 2^16)
    dp = [[0.0] * (1 << 16) for _ in range(n + 1)]

    # Base case: the first ticket has 2 possible unique number combinations
    dp[0][0] = 1.0

    for i in range(1, n + 1):
        prev_used = set()
        for j in range(i):
            # Iterate over all possible subsets of used numbers
            for mask in range((1 << 16) - 1, -1, -1):
                if bin(mask).count('1') == len(prev_used):
                    break
            for k in range(2):  # Consider both options (A and B)
                new_mask = mask ^ (1 << prev_used.pop())
                dp[i][new_mask] += dp[j][mask] * ((k == 0) or (1 - float(k)) / 2)

    return sum(dp[-1])  # Calculate the final probability

# Read input
T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    probabilities = []
    for _ in range(n):
        p, a, b = map(int, sys.stdin.readline().split())
        probabilities.append((p, a, b))
    print("{:.6f}".format(correct_numbering(n)))
