from collections import defaultdict

def winning_teams(n):
    # Initialize memo dictionary
    memo = defaultdict(int)

    # Base case: only one team left, so it's the winner
    for i in range(2**n):
        memo[(0, 1 << i)] = (i & 1) * [i]

    # Dynamic programming loop
    for i in range(n - 1, -1, -1):
        for j in range(1 << (n - i), -1, -1):
            if not (j & (1 << i)):
                # Team i loses, so no new teams can win
                continue

            prev_i = i + 1
            prev_j = j ^ (1 << i)
            max_skill = memo[(prev_i, prev_j)]

            for k in range(n - i):
                if not (j & (1 << (i + k))):
                    # Team i+k loses, so no new teams can win
                    continue

                next_j = prev_j ^ (1 << (i + k))
                new_skill = max_skill + [(i + k) & 1]

                memo[(i, j)] = min(memo.get((i, j), float('inf')), new_skill)

    # Find all winning teams and print them
    for i in range(2**n):
        if len(memo[(0, 1 << i)]) > 0:
            print(*memo[(0, 1 << i)])

# Example usage
n = int(input())  # Get the number of phases from stdin
winning_teams(n)
