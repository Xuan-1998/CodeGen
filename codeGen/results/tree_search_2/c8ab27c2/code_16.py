def min_uncommon_length(S, T):
    # Create a set to store all subsequences of T
    T_subsequences = {"".join(sorted(c)) for t in T for c in [t[i: j] for i in range(len(t)) for j in range(i + 1, len(t) + 1)]}

    shortest_length = float('inf')
    for length in range(1, len(S) + 1):
        for i in range(len(S) - length + 1):
            subsequence = S[i: i + length]
            # Check if the current subsequence is not in T_subsequences
            if "".join(sorted(subsequence)) not in T_subsequences:
                return length

    return -1  # If no uncommon subsequences are found, return -1


# Test the function with example inputs
S = input().strip()
T = [input().strip() for _ in range(int(input()))]
print(min_uncommon_length(S, T))
