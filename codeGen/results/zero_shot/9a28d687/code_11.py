import sys

def calculate_cost():
    # Read the input
    n = int(sys.stdin.readline().strip())
    cost_list = list(map(int, sys.stdin.readline().strip().split()))
    string_list = [sys.stdin.readline().strip() for _ in range(n)]

    # Initialize a 2D DP table to store the minimum cost for each prefix of the strings and their reversals
    dp_table = [[0] * (n + 1) for _ in range(2 ** n + 1)]

    # Fill up the DP table
    for i in range(2 ** n):
        prefix = ''
        for j in range(n):
            if ((i >> j) & 1):
                prefix += string_list[j][::-1]
            else:
                prefix += string_list[j]
        for k in range(len(prefix)):
            cost = sum(cost_list[ord(c) - ord('a')] for c in prefix[:k + 1])
            dp_table[i][k] = min(dp_table[i][k], cost)

    # Find the minimum cost to sort all strings
    total_cost = float('inf')
    for i in range(n):
        prefix_cost = dp_table[2 ** n - 1][i]
        reversal_cost = sum(cost_list[ord(c) - ord('a')] for c in string_list[i][::-1])
        total_cost = min(total_cost, prefix_cost + reversal_cost)

    # Check if the strings can be sorted lexicographically
    if total_cost == float('inf'):
        print(-1)
    else:
        print(total_cost)

if __name__ == "__main__":
    calculate_cost()
