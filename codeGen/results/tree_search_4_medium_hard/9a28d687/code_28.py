from collections import defaultdict

def sort_strings_by_cost(n, costs, strings):
    # Initialize memoization table
    dp = [[-1] * n for _ in range(n)]

    # Base case: only one string to be sorted
    for i in range(n):
        dp[0][i] = costs[i]

    # Fill up the memoization table using bottom-up approach
    for i in range(1, n):
        for j in range(i):
            if strings[j] < strings[i]:
                prefix_lengths = [len(strings[i].lstrip(string)) for string in strings[:j]]
                for length in range(min(prefix_lengths), 0, -1):
                    if all(s[:length] == strings[i][:length] for s in strings[:j]):
                        dp[i][j] = min(dp[i][j], dp[i-1][k] + costs[j] for k in range(j))
                        break
                else:
                    dp[i][j] = -1

    # Find the minimum total cost to sort all strings
    return min(dp[-1])

# Read input from stdin
n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

print(sort_strings_by_cost(n, costs, strings))
