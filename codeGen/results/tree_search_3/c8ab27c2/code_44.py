def shortest_uncommon_subsequence(S, T):
    # Find the LCS of S and T
    m = len(S)
    n = len(T)
    i = j = 0
    lcs = []
    while i < m and j < n:
        if S[m - 1 - i] == T[n - 1 - j]:
            lcs.append(S[m - 1 - i])
            i += 1
            j += 1
        elif S[m - 1 - i] < T[n - 1 - j]:
            i += 1
        else:
            j += 1

    # Reverse the LCS to get the correct order
    lcs = ''.join(reversed(lcs))

    # Calculate the length of the shortest uncommon subsequence
    return max(len(S) - len(lcs), len(T) - len(lcs))

# Read input from standard input
S, T = input().split()

# Print the output to standard output
print(shortest_uncommon_subsequence(S, T))
