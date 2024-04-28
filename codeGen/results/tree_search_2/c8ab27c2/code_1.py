def shortest_uncommon_subsequence(S, T):
    n = len(S)
    m = len(T)

    # Initialize a dictionary to store the lengths of subsequences
    dp = {(0, 0): float('inf')}

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] == T[j - 1]:
                # If the current characters match, update the dictionary accordingly
                dp[(i, j)] = dp.get((i - 1, j - 1), float('inf')) - 1
            else:
                # If the current characters don't match, consider both possibilities
                dp[(i, j)] = min(dp.get((i - 1, j), float('inf')), dp.get((i, j - 1), float('inf')))

    # Find the shortest uncommon subsequence by iterating over all possible lengths
    shortest_length = float('inf')
    for i in range(n + 1):
        if (n, m) not in [k for k in dp.keys() if k[0] <= i and k[1] <= m]:
            shortest_length = min(shortest_length, i)

    return -1 if shortest_length == float('inf') else shortest_length
