def find_shortest_uncommon_subsequence():
    s = input().strip()
    t = input().strip()

    # Initialize variables to store the lengths of S and T
    length_s = len(s)
    length_t = len(t)

    # Initialize variables to store the longest common suffix (LCS) found so far
    lcs_length = 0

    # Iterate through both strings from right to left
    for i in range(length_s, -1, -1):
        for j in range(length_t, -1, -1):
            if s[i] == t[j]:
                # If the current characters match, update the LCS length
                lcs_length += 1
                if i == 0 or j == 0:
                    break
            else:
                # If they do not match, update the LCS length to be 0 and break the inner loop
                lcs_length = 0
                break

    # The length of the shortest uncommon subsequence is given by subtracting the LCS length from the lengths of S and T
    return abs(length_s - length_t) - lcs_length


print(find_shortest_uncommon_subsequence())
